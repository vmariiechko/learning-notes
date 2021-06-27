using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Client
{
    public partial class Board : Form
    {
        private delegate void UpdateMapProc(byte[] tmp);
        private delegate void UpdateStatusProc(string message);
        private delegate void AdjustControlsProc();

        private UInt16 Port = 4201;
        private bool IsConnected = false;
        private TcpClient client;

        const int mapSize = 8;
        const int cellSize = 50;

        int currentPlayer;
        int playerColor;

        List<Button> simpleSteps = new List<Button>();

        int countEatSteps = 0;
        Button prevButton;
        Button pressedButton;
        bool isContinue = false;

        bool isMoving;

        int[,] map = new int[mapSize, mapSize];

        Button[,] buttons = new Button[mapSize, mapSize];

        Image whiteFigure;
        Image blackFigure;

        public Board()
        {
            InitializeComponent();
            //whiteFigure = new Bitmap(new Bitmap(@"C:\Users\vadim\Desktop\white.png"), new Size(cellSize - 10, cellSize - 10));
            //blackFigure = new Bitmap(new Bitmap(@"C:\Users\vadim\Desktop\black.png"), new Size(cellSize - 10, cellSize - 10));
            whiteFigure = new Bitmap(new Bitmap(@"..\..\Sprites\white.png"), new Size(cellSize - 10, cellSize - 10));
            blackFigure = new Bitmap(new Bitmap(@"..\..\Sprites\black.png"), new Size(cellSize - 10, cellSize - 10));
            Init();
        }


        public void Init()
        {
            currentPlayer = 1;
            isMoving = false;
            prevButton = null;
            txtPort.Text = Port.ToString();
            map = new int[mapSize, mapSize] {
                { 0,1,0,1,0,1,0,1 },
                { 1,0,1,0,1,0,1,0 },
                { 0,1,0,1,0,1,0,1 },
                { 0,0,0,0,0,0,0,0 },
                { 0,0,0,0,0,0,0,0 },
                { 2,0,2,0,2,0,2,0 },
                { 0,2,0,2,0,2,0,2 },
                { 2,0,2,0,2,0,2,0 }
            };
            CreateMap();
            AdjustControls();
        }

        public void ResetGame()
        {
            bool player1 = false;
            bool player2 = false;
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    if (map[i, j] == 1) player1 = true;
                    if (map[i, j] == 2) player2 = true;
                }
            }
            if (!player1 || !player2)
            {
                ReloadBoard();
            }
        }

        public void ReloadBoard()
        {
            this.Controls.Clear();
            InitializeComponent();
            Init();
        }

        public void CreateMap()
        {
            this.Width = (mapSize + 1) * cellSize + txtHost.Width;
            this.Height = (mapSize + 1) * cellSize;
            for (int r = 0; r < mapSize; r++)
            {
                for (int c = 0; c < mapSize; c++)
                {
                    Button button = new Button();
                    button.Location = new Point(c * cellSize, r * cellSize);
                    button.Size = new Size(cellSize, cellSize);
                    button.Click += new EventHandler(OnFigurePress);
                    if (map[r, c] == 1) button.Image = whiteFigure;
                    else if (map[r, c] == 2) button.Image = blackFigure;
                    button.BackColor = GetPrevButtonColor(button);
                    button.ForeColor = Color.White;
                    button.Font = new Font("Microsoft Sans Serif", 12F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(204)));
                    buttons[r, c] = button;
                    this.Controls.Add(button);
                }
            }
            RelocateForm();
        }

        public void RelocateForm()
        {
            int x = 15 + mapSize * cellSize;
            lbHost.Location = new Point(x, mapSize);
            txtHost.Location = new Point(x, mapSize + cellSize / 3);
            lbPort.Location = new Point(x, mapSize + cellSize - 10);
            txtPort.Location = new Point(x, mapSize + cellSize + 5);
            btnConnect.Location = new Point(x, mapSize + 2 * cellSize);
            lbColor.Location = new Point(x, mapSize + 3 * cellSize);
            lbStatus.Location = new Point(x, mapSize + 4 * cellSize);
            txtStatus.Location = new Point(x, mapSize + 4 * cellSize + 15);
        }

        public void UpdateMap(byte[] btnsPos)
        {
            if (InvokeRequired) Invoke(new UpdateMapProc(UpdateMap), btnsPos);
            else
            {
                if (btnsPos[4] == 1)
                {
                    SwitchPlayer();
                    if (currentPlayer == playerColor)
                    {
                        UpdateStatus("Your turn to move");
                        ShowPossibleSteps();
                    }
                    else UpdateStatus("Waiting for opponent move...");
                }
                else
                {
                    prevButton = buttons[btnsPos[0], btnsPos[1]];
                    pressedButton = buttons[btnsPos[2], btnsPos[3]];
                    int temp = map[btnsPos[2], btnsPos[3]];
                    map[btnsPos[2], btnsPos[3]] = map[btnsPos[0], btnsPos[1]];
                    map[btnsPos[0], btnsPos[1]] = temp;
                    pressedButton.Image = prevButton.Image;
                    prevButton.Image = null;
                    pressedButton.Text = prevButton.Text;
                    prevButton.Text = "";
                    if (Math.Abs(pressedButton.Location.X / cellSize - prevButton.Location.X / cellSize) > 1)
                    {
                        DeleteEaten(pressedButton, prevButton);
                    }
                    SwitchButtonToCheat(pressedButton);
                    prevButton = pressedButton;
                }
            }
        }

        private void UpdateStatus(string message)
        {
            if (InvokeRequired) Invoke(new UpdateStatusProc(UpdateStatus), message);
            else txtStatus.Text = message;
        }

        private void UpdateColor(string message)
        {
            if (InvokeRequired) Invoke(new UpdateStatusProc(UpdateColor), message);
            else lbColor.Text = message;
        }

        private void AdjustControls()
        {
            if (InvokeRequired) Invoke(new AdjustControlsProc(AdjustControls));
            else
            {
                if (IsConnected)
                {
                    txtHost.Enabled = false;
                    txtPort.Enabled = false;
                    btnConnect.Text = "Disconnect";
                }
                else
                {
                    txtHost.Enabled = true;
                    txtPort.Enabled = true;
                    btnConnect.Text = "Connect";
                    lbColor.Text = "";
                }
            }
        }

        public void SwitchPlayer()
        {
            currentPlayer = currentPlayer == 1 ? 2 : 1;
            ResetGame();
        }

        public Color GetPrevButtonColor(Button prevButton)
        {
            if ((prevButton.Location.Y) / cellSize % 2 != 0)
            {
                if ((prevButton.Location.X / cellSize) % 2 == 0)
                {
                    return Color.Gray;
                }
            }
            if ((prevButton.Location.Y / cellSize) % 2 == 0)
            {
                if ((prevButton.Location.X / cellSize) % 2 != 0)
                {
                    return Color.Gray;
                }
            }
            return Color.White;
        }

        public void OnFigurePress(object sender, EventArgs e)
        {
            if (prevButton != null)
                prevButton.BackColor = GetPrevButtonColor(prevButton);

            pressedButton = sender as Button;

            if (map[pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize] != 0 && map[pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize] == currentPlayer && currentPlayer == playerColor)
            {
                CloseSteps();
                pressedButton.BackColor = Color.Red;
                DeactivateAllButtons();
                pressedButton.Enabled = true;
                countEatSteps = 0;
                if (pressedButton.Text == "K")
                    ShowSteps(pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize, false);
                else ShowSteps(pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize);

                if (isMoving)
                {
                    CloseSteps();
                    pressedButton.BackColor = GetPrevButtonColor(pressedButton);
                    ShowPossibleSteps();
                    isMoving = false;
                }
                else
                    isMoving = true;
            }
            else
            {
                if (isMoving)
                {
                    isContinue = false;
                    if (Math.Abs(pressedButton.Location.X / cellSize - prevButton.Location.X / cellSize) > 1)
                    {
                        isContinue = true;
                        DeleteEaten(pressedButton, prevButton);
                    }
                    SendMove();
                    countEatSteps = 0;
                    isMoving = false;
                    CloseSteps();
                    DeactivateAllButtons();
                    if (pressedButton.Text == "K")
                        ShowSteps(pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize, false);
                    else ShowSteps(pressedButton.Location.Y / cellSize, pressedButton.Location.X / cellSize);
                    if (countEatSteps == 0 || !isContinue)
                    {
                        CloseSteps();
                        SendMove(true);
                        ShowPossibleSteps();
                        isContinue = false;
                    }
                    else if (isContinue)
                    {
                        pressedButton.BackColor = Color.Red;
                        pressedButton.Enabled = true;
                        isMoving = true;
                    }
                }
            }
            prevButton = pressedButton;
        }

        public void ShowPossibleSteps()
        {
            bool isOneStep = true;
            bool isEatStep = false;
            DeactivateAllButtons();
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    if (map[i, j] == currentPlayer)
                    {
                        if (buttons[i, j].Text == "K") isOneStep = false;
                        else isOneStep = true;
                        if (IsButtonHasEatStep(i, j, isOneStep, new int[2] { 0, 0 }))
                        {
                            isEatStep = true;
                            buttons[i, j].Enabled = true;
                        }
                    }
                }
            }
            if (!isEatStep) ActivateAllButtons();
        }

        public void SwitchButtonToCheat(Button button)
        {
            if (map[button.Location.Y / cellSize, button.Location.X / cellSize] == 1 && button.Location.Y / cellSize == mapSize - 1)
            {
                button.Text = "K";
            }
            if (map[button.Location.Y / cellSize, button.Location.X / cellSize] == 2 && button.Location.Y / cellSize == 0)
            {
                button.Text = "K";
            }
        }

        public void DeleteEaten(Button endButton, Button startButton)
        {
            int count = Math.Abs(endButton.Location.Y / cellSize - startButton.Location.Y / cellSize);
            int startIndexX = endButton.Location.Y / cellSize - startButton.Location.Y / cellSize;
            int startIndexY = endButton.Location.X / cellSize - startButton.Location.X / cellSize;
            startIndexX = startIndexX < 0 ? -1 : 1;
            startIndexY = startIndexY < 0 ? -1 : 1;
            int currCount = 0;
            int i = startButton.Location.Y / cellSize + startIndexX;
            int j = startButton.Location.X / cellSize + startIndexY;
            while (currCount < count - 1)
            {
                map[i, j] = 0;
                buttons[i, j].Image = null;
                buttons[i, j].Text = "";
                i += startIndexX;
                j += startIndexY;
                currCount++;
            }

        }

        public void ShowSteps(int iCurrFigure, int jCurrFigure, bool isOnestep = true)
        {
            simpleSteps.Clear();
            ShowDiagonal(iCurrFigure, jCurrFigure, isOnestep);
            if (countEatSteps > 0) CloseSimpleSteps(simpleSteps);
        }

        public void ShowDiagonal(int IcurrFigure, int JcurrFigure, bool isOneStep = false)
        {
            int j = JcurrFigure + 1;
            for (int i = IcurrFigure - 1; i >= 0; i--)
            {
                if (currentPlayer == 1 && isOneStep && !isContinue) break;
                if (IsInsideBorders(i, j))
                {
                    if (!DeterminePath(i, j))
                        break;
                }
                if (j < 7)
                    j++;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure - 1;
            for (int i = IcurrFigure - 1; i >= 0; i--)
            {
                if (currentPlayer == 1 && isOneStep && !isContinue) break;
                if (IsInsideBorders(i, j))
                {
                    if (!DeterminePath(i, j))
                        break;
                }
                if (j > 0)
                    j--;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure - 1;
            for (int i = IcurrFigure + 1; i < 8; i++)
            {
                if (currentPlayer == 2 && isOneStep && !isContinue) break;
                if (IsInsideBorders(i, j))
                {
                    if (!DeterminePath(i, j))
                        break;
                }
                if (j > 0)
                    j--;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure + 1;
            for (int i = IcurrFigure + 1; i < 8; i++)
            {
                if (currentPlayer == 2 && isOneStep && !isContinue) break;
                if (IsInsideBorders(i, j))
                {
                    if (!DeterminePath(i, j))
                        break;
                }
                if (j < 7)
                    j++;
                else break;

                if (isOneStep)
                    break;
            }
        }

        public bool DeterminePath(int ti, int tj)
        {

            if (map[ti, tj] == 0 && !isContinue)
            {
                buttons[ti, tj].BackColor = Color.Yellow;
                buttons[ti, tj].Enabled = true;
                simpleSteps.Add(buttons[ti, tj]);
            }
            else
            {

                if (map[ti, tj] != currentPlayer)
                {
                    if (pressedButton.Text == "K")
                        ShowProceduralEat(ti, tj, false);
                    else ShowProceduralEat(ti, tj);
                }

                return false;
            }
            return true;
        }

        public void CloseSimpleSteps(List<Button> simpleSteps)
        {
            if (simpleSteps.Count > 0)
            {
                for (int i = 0; i < simpleSteps.Count; i++)
                {
                    simpleSteps[i].BackColor = GetPrevButtonColor(simpleSteps[i]);
                    simpleSteps[i].Enabled = false;
                }
            }
        }

        public void ShowProceduralEat(int i, int j, bool isOneStep = true)
        {
            int dirX = i - pressedButton.Location.Y / cellSize;
            int dirY = j - pressedButton.Location.X / cellSize;
            dirX = dirX < 0 ? -1 : 1;
            dirY = dirY < 0 ? -1 : 1;
            int il = i;
            int jl = j;
            bool isEmpty = true;
            while (IsInsideBorders(il, jl))
            {
                if (map[il, jl] != 0 && map[il, jl] != currentPlayer)
                {
                    isEmpty = false;
                    break;
                }
                il += dirX;
                jl += dirY;

                if (isOneStep)
                    break;
            }
            if (isEmpty)
                return;
            List<Button> toClose = new List<Button>();
            bool closeSimple = false;
            int ik = il + dirX;
            int jk = jl + dirY;
            while (IsInsideBorders(ik, jk))
            {
                if (map[ik, jk] == 0)
                {
                    if (IsButtonHasEatStep(ik, jk, isOneStep, new int[2] { dirX, dirY }))
                    {
                        closeSimple = true;
                    }
                    else
                    {
                        toClose.Add(buttons[ik, jk]);
                    }
                    buttons[ik, jk].BackColor = Color.Yellow;
                    buttons[ik, jk].Enabled = true;
                    countEatSteps++;
                }
                else break;
                if (isOneStep)
                    break;
                jk += dirY;
                ik += dirX;
            }
            if (closeSimple && toClose.Count > 0)
            {
                CloseSimpleSteps(toClose);
            }

        }

        public bool IsButtonHasEatStep(int IcurrFigure, int JcurrFigure, bool isOneStep, int[] dir)
        {
            bool eatStep = false;
            int j = JcurrFigure + 1;
            for (int i = IcurrFigure - 1; i >= 0; i--)
            {
                if (currentPlayer == 1 && isOneStep && !isContinue) break;
                if (dir[0] == 1 && dir[1] == -1 && !isOneStep) break;
                if (IsInsideBorders(i, j))
                {
                    if (map[i, j] != 0 && map[i, j] != currentPlayer)
                    {
                        eatStep = true;
                        if (!IsInsideBorders(i - 1, j + 1))
                            eatStep = false;
                        else if (map[i - 1, j + 1] != 0)
                            eatStep = false;
                        else return eatStep;
                    }
                }
                if (j < 7)
                    j++;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure - 1;
            for (int i = IcurrFigure - 1; i >= 0; i--)
            {
                if (currentPlayer == 1 && isOneStep && !isContinue) break;
                if (dir[0] == 1 && dir[1] == 1 && !isOneStep) break;
                if (IsInsideBorders(i, j))
                {
                    if (map[i, j] != 0 && map[i, j] != currentPlayer)
                    {
                        eatStep = true;
                        if (!IsInsideBorders(i - 1, j - 1))
                            eatStep = false;
                        else if (map[i - 1, j - 1] != 0)
                            eatStep = false;
                        else return eatStep;
                    }
                }
                if (j > 0)
                    j--;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure - 1;
            for (int i = IcurrFigure + 1; i < 8; i++)
            {
                if (currentPlayer == 2 && isOneStep && !isContinue) break;
                if (dir[0] == -1 && dir[1] == 1 && !isOneStep) break;
                if (IsInsideBorders(i, j))
                {
                    if (map[i, j] != 0 && map[i, j] != currentPlayer)
                    {
                        eatStep = true;
                        if (!IsInsideBorders(i + 1, j - 1))
                            eatStep = false;
                        else if (map[i + 1, j - 1] != 0)
                            eatStep = false;
                        else return eatStep;
                    }
                }
                if (j > 0)
                    j--;
                else break;

                if (isOneStep)
                    break;
            }

            j = JcurrFigure + 1;
            for (int i = IcurrFigure + 1; i < 8; i++)
            {
                if (currentPlayer == 2 && isOneStep && !isContinue) break;
                if (dir[0] == -1 && dir[1] == -1 && !isOneStep) break;
                if (IsInsideBorders(i, j))
                {
                    if (map[i, j] != 0 && map[i, j] != currentPlayer)
                    {
                        eatStep = true;
                        if (!IsInsideBorders(i + 1, j + 1))
                            eatStep = false;
                        else if (map[i + 1, j + 1] != 0)
                            eatStep = false;
                        else return eatStep;
                    }
                }
                if (j < 7)
                    j++;
                else break;

                if (isOneStep)
                    break;
            }
            return eatStep;
        }

        public bool IsInsideBorders(int ti, int tj)
        {
            if (ti >= mapSize || tj >= mapSize || ti < 0 || tj < 0)
            {
                return false;
            }
            return true;
        }

        public void CloseSteps()
        {
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    buttons[i, j].BackColor = GetPrevButtonColor(buttons[i, j]);
                }
            }
        }

        public void ActivateAllButtons()
        {
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    buttons[i, j].Enabled = true;
                }
            }
        }

        public void DeactivateAllButtons()
        {
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    buttons[i, j].Enabled = false;
                }
            }
        }

        private void TxtPort_TextChanged(object sender, EventArgs e)
        {
            btnConnect.Enabled = UInt16.TryParse(txtPort.Text, out Port);
        }

        private void ClientThread()
        {
            try
            {
                client = new TcpClient(txtHost.Text.Trim(), Port);
            }
            catch (SocketException)
            {
                UpdateStatus("Server is offline");
                return;
            }
            Socket socket = client.Client;
            bool first = true;
            UpdateStatus("Connected");
            IsConnected = true;
            AdjustControls();
            while (IsConnected)
            {
                if (socket.Poll(50000, SelectMode.SelectRead))
                {
                    int size = socket.Available;
                    if (size <= 0) break;
                    byte[] buffor = new byte[size];
                    socket.Receive(buffor);
                    if (first)
                    {
                        playerColor = buffor[0] + 1;
                        string color = playerColor == 1 ? "white" : "black";
                        UpdateColor($"You are playing for {color}");
                        if (currentPlayer == playerColor) UpdateStatus("Your turn to move");
                        else UpdateStatus("Waiting for opponent move...");
                        first = false;
                    }
                    else UpdateMap(buffor);
                }
            }
            AdjustControls();
            UpdateStatus("Disconnected");
            socket.Disconnect(true);
        }

        public void SendMove(bool switchPlayer = false)
        {
            byte[] buffor = new byte[5];
            if (switchPlayer) buffor[4] = 1;
            else
            {
                buffor[0] = (byte)(prevButton.Location.Y / cellSize);
                buffor[1] = (byte)(prevButton.Location.X / cellSize);
                buffor[2] = (byte)(pressedButton.Location.Y / cellSize);
                buffor[3] = (byte)(pressedButton.Location.X / cellSize);
            }
            try
            {
                client.Client.Send(buffor);
            }
            catch (SocketException)
            {
                UpdateStatus("You have been disconnected");
                return;
            }
        }

        private void BtnConnect_Click(object sender, EventArgs e)
        {
            if (IsConnected)
            {
                ReloadBoard();
                IsConnected = false;
            }
            else new Thread(ClientThread).Start();
            AdjustControls();
        }

    }
}

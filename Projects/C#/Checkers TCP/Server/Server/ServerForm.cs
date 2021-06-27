using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Server
{
    public partial class ServerForm : Form
    {
        private delegate void LogAddProc(string message);
        private delegate void AdjustControlsProc();
        private UInt16 port = 4201;
        private byte newClientId = 1;
        private bool IsConnected;
        private TcpListener server;
        private Dictionary<byte, Socket> clients = new Dictionary<byte, Socket>();
        public ServerForm()
        {
            InitializeComponent();
            txtPort.Text = port.ToString();
        }

        private void LogAdd(string message)
        {
            if (InvokeRequired) Invoke(new LogAddProc(LogAdd), message);
            else txtLog.AppendText(message + Environment.NewLine);
        }

        private void AdjustControls()
        {
            if (InvokeRequired) Invoke(new AdjustControlsProc(AdjustControls));
            else
            {
                if (IsConnected)
                {
                    txtPort.Enabled = false;
                    btnConnect.Text = "Disconnect";
                }
                else
                {
                    txtPort.Enabled = true;
                    btnConnect.Text = "Connect";
                }
            }
        }

        private void txtPort_TextChanged(object sender, EventArgs e)
        {
            btnConnect.Enabled = UInt16.TryParse(txtPort.Text, out port);
        }

        public void ServerThread()
        {
            server = new TcpListener(IPAddress.Any, port);
            server.Start();
            LogAdd("Server connected");
            IsConnected = true;
            AdjustControls();
            while (IsConnected)
            {
                if (server.Pending()) new Thread(ServerClientThread).Start();
            }
            IsConnected = false;
            AdjustControls();
            LogAdd("Server disconnected");
            server.Stop();
        }

        private void ServerClientThread()
        {
            Socket socket;
            try
            {
                socket = server.AcceptSocket();
            }
            catch (SocketException)
            {
                return;
            }

            string who = socket.RemoteEndPoint.ToString();
            byte currentClientId = newClientId++;
            byte clientSide = (byte)(currentClientId % 2);
            lock (clients) clients.Add(currentClientId, socket);
            LogAdd("Client connected " + who);
            socket.Send(new byte[] { clientSide });
            while (IsConnected)
            {
                if (socket.Poll(50000, SelectMode.SelectRead))
                {
                    int size = socket.Available;
                    if (size <= 0) break;
                    byte[] buffor = new byte[size];
                    socket.Receive(buffor);
                    lock (clients)
                    {
                        clients[currentClientId].Send(buffor);
                        if (clientSide == 0) clients[(byte)(currentClientId - 1)].Send(buffor);
                        else clients[(byte)(currentClientId + 1)].Send(buffor);
                    }
                }
            }
            LogAdd("Client" + who + " disconnected");
            lock (clients) clients.Remove(currentClientId);
            socket.Disconnect(false);
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            if (IsConnected) IsConnected = false;
            else new Thread(ServerThread).Start();
            AdjustControls();
        }
    }
}

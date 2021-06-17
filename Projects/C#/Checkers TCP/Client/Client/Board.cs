using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Client
{
    public partial class Board : Form
    {
        private const int mapSize = 8;
        private const int cellSize = 50;

        private Image whiteFigure;
        private Image blackFigure;

        int[,] map = new int[mapSize, mapSize];
        public Board()
        {
            InitializeComponent();

            whiteFigure = new Bitmap(new Bitmap(@"C:\Users\vadim\Desktop\white.png"), new Size(cellSize - 10, cellSize - 10));
            blackFigure = new Bitmap(new Bitmap(@"C:\Users\vadim\Desktop\black.png"), new Size(cellSize - 10, cellSize - 10));

            Init();
        }


        public void Init()
        {
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
        }

        public void CreateMap()
        {
            this.Width = (mapSize + 1) * cellSize;
            this.Height = (mapSize + 1) * cellSize;

            for (int i = 0; i < mapSize; ++i)
            {
                for (int j = 0; j < mapSize; ++j)
                {
                    Button button = new Button();
                    button.Location = new Point(j * cellSize, i * cellSize);
                    button.Size = new Size(cellSize, cellSize);
                    if (map[i, j] == 1) button.Image = whiteFigure;
                    else if (map[i, j] == 2) button.Image = blackFigure;
                    if (i % 2 != 0)
                    {
                        if (j % 2 == 0)
                        {
                            button.BackColor = Color.Gray;
                        }
                    }
                    if (i % 2 == 0)
                    {
                        if (j % 2 != 0)
                        {
                            button.BackColor = Color.Gray;
                        }
                    }
                    this.Controls.Add(button);
                }
            }
        }
    }
}
const express = require('express');
const multer = require('multer');
const Jimp = require('jimp');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public'));

// Configure multer for in-memory storage
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

async function analyzeImage(imageBuffer) {
  try {
    const image = await Jimp.read(imageBuffer);
    const width = image.bitmap.width;
    const height = image.bitmap.height;

    // Definimos la cuadrícula: 30 columnas x 6 filas
    const gridColumns = 30;
    const gridRows = 6;
    
    // Calculamos el tamaño de cada celda
    const cellWidth = width / gridColumns;
    const cellHeight = height / gridRows;
    
    // Matriz para almacenar los resultados
    const grid = [];

    // Analizamos cada celda de la cuadrícula
    for (let row = 0; row < gridRows; row++) {
      grid[row] = [];
      for (let col = 0; col < gridColumns; col++) {
        // Punto central de la celda
        const x = Math.floor((col + 0.5) * cellWidth);
        const y = Math.floor((row + 0.5) * cellHeight);
        
        // Obtenemos el color del píxel central
        const color = Jimp.intToRGBA(image.getPixelColor(x, y));
        
        // Mejoramos la detección de color con umbrales más precisos
        if (color.r > 150 && color.g < 100 && color.b < 100) {
          grid[row][col] = "R"; // Rojo
        } else if (color.b > 150 && color.r < 100 && color.g < 100) {
          grid[row][col] = "B"; // Azul
        } else {
          grid[row][col] = "-"; // Vacío o no detectado
        }
      }
    }

    return grid;
  } catch (error) {
    console.error(`Error procesando la imagen:`, error);
    throw new Error('Error al procesar la imagen');
  }
}

app.post('/analyze', upload.single('image'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No se subió ninguna imagen.' });
  }

  try {
    const grid = await analyzeImage(req.file.buffer);
    res.json({ grid });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
}); 
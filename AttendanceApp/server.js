// server.js

const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3001;

app.use(express.json());

app.post('/add-face', (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ error: 'Name is required' });
  }

  exec(`python addData.py ${name}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    console.log(`stdout: ${stdout}`);
    res.status(200).json({ message: `Face added for ${name}` });
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

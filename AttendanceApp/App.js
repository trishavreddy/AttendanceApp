// App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [studentName, setStudentName] = useState('');

  const handleNameChange = (event) => {
    setStudentName(event.target.value);
  };

  const handleSubmit = () => {
    // Handle form submission
  };

  return (
    <div className="App">
      <h1>Student Attendance System</h1>
      <h2>Add Your Face</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={studentName} onChange={handleNameChange} />
        </label>
        <button type="submit">Add Face</button>
      </form>
    </div>
  );
}

export default App;

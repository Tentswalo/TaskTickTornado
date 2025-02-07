import React, { useState } from 'react';
import axios from 'axios';

const AddTask = () => {
  const [name, setName] = useState('');
  const [priority, setPriority] = useState('Low');
  const [dueDate, setDueDate] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/tasks', {
        name,
        priority,
        dueDate,
        userId: 1, // Replace with dynamic user ID
      });
      console.log('Task added:', response.data);
      setName('');
      setPriority('Low');
      setDueDate('');
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  return (
    <div>
      <h2>Add Task</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Task Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <select value={priority} onChange={(e) => setPriority(e.target.value)}>
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>
        <input
          type="date"
          value={dueDate}
          onChange={(e) => setDueDate(e.target.value)}
          required
        />
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
};

export default AddTask;
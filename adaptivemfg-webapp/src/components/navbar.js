import React from 'react';
import { Link } from 'react-router-dom'; // Assuming you're using React Router

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>AdaptiveMFG</h1>
      <ul>
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/add-machine">Add Machine</Link></li>
        <li><Link to="/history">History</Link></li>
        <li><Link to="/alerts">Alerts</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;

import React from 'react';
import './App.css';
import { Link } from 'react-router-dom';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const Home = () => {
  return (
    <div>
        <Link to="/books">See book list</Link>
    </div>
  );
}

export default Home;

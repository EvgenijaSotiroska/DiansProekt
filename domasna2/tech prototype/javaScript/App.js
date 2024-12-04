import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import BookList from './StockList';


function App() {

 return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home/>}/>
        <Route path='/stock' exact={true} element={<StockList/>}/>
      </Routes>
    </Router>
  );
}

export default App;

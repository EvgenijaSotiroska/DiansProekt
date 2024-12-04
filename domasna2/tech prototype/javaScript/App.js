import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import BookList from './BookList';


function App() {
/*  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8080/api/books/all')
 //   .then(response => console.log(response.json()));
      .then(response => response.json())
      .then(data => {
        setBooks(data);
      })
  }
  , []);

  const bookList = books.map(book => {
    return <tr key={book.id}>
      <td>{book.bookName}</td>
      <td>{book.author}</td>
      <td>{book.price}</td>
      <td>{book.isInStock.toString()}</td>
    </tr>
  });
*/

  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home/>}/>
        <Route path='/books' exact={true} element={<BookList/>}/>
      </Routes>
    </Router>
  );
}

export default App;

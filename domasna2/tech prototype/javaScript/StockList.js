import React, { useEffect, useState } from 'react';

const StockList = () => {
        const [stocks, setStocks] = useState([]);
      
        useEffect(() => {
          fetch('http://localhost:8080/api/stock/all')
       //   .then(response => console.log(response.json()));
            .then(response => response.json())
            .then(data => {
              setStocks(data);
            })
        }
        , []);
      
        const stockList = stocks.map(stock => {
          return <tr key={stock.id}>
            <td>{stock.code}</td>
            <td>{stock.turnover}</td>
            <td>{stock.totalturnover}</td>
          </tr>
        });
      
      
        return (
          <div className="App">
            <header className="App-header">
              <div className="App-intro">
                <h2>Stock List</h2>
                <table className="mt-4">
                <thead>
                <tr>
                  <th>Code</th>
                  <th>Turnover</th>
                  <th>totalturnover</th>
                </tr>
                </thead>
                <tbody>
                {stockList}
                </tbody>
              </table>
              </div>
            </header>
          </div>
        );
    }

export default StockList;
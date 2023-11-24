import React, { useState, useEffect } from 'react';

function SalesList() {
  const [sales, setSales] = useState([]);

  useEffect(() => {
    const fetchSales = async () => {
      try {
        console.log('Fetching sales...');
        const response = await fetch('http://localhost:5000/sales');
        console.log('Response received', response);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Data:', data);
        setSales(data);
      } catch (error) {
        console.error("Could not fetch sales:", error);
      }
    };
  
    fetchSales();
  }, []);


  const saleListStyle = {
    margin: 0,
    padding: 0,
    listStyle: 'none'   
  }

  const saleListItemStyle = {
    margin: '10px 0',
    padding: '5px',
    borderBottom: '1px solid #ccc' 
  }



  return (
    <div>
      <h2>Sales List</h2>
      <ul style = {saleListStyle}>
        {sales.map(sale => (
          <li style = {saleListItemStyle} key={sale.id}>{sale.name} - ${sale.price}</li>
        ))}
      </ul>
    </div>
  );
  
}

export default SalesList;
import React, { useState, useEffect } from 'react';

function CustomersList() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        console.log('Fetching customers...');
        const response = await fetch('http://localhost:5000/customer');
        console.log('Response received', response);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Data:', data);
        setCustomers(data);
      } catch (error) {
        console.error("Could not fetch customers:", error);
      }
    };
  
    fetchCustomers();
  }, []);


  const customerListStyle = {
    margin: 0,
    padding: 0,
    listStyle: 'none'   
  }

  const customerListItemStyle = {
    margin: '10px 0',
    padding: '5px',
    borderBottom: '1px solid #ccc' 
  }



  return (
    <div>
      <h2>Customers List</h2>
      <ul style = {customerListStyle}>
        {customers.map(sale => (
          <li style = {customerListItemStyle} key={customers.id}>{customers.name} - ${customers.price}</li>
        ))}
      </ul>
    </div>
  );
  
}

export default CustomersList;
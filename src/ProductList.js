import React, { useState, useEffect } from 'react';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        console.log('Fetching products...');
        const response = await fetch('http://localhost:5000/products');
        console.log('Response received', response);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Data:', data);
        setProducts(data);
      } catch (error) {
        console.error("Could not fetch products:", error);
      }
    };
  
    fetchProducts();
  }, []);


  const productListStyle = {
    margin: 0,
    padding: 0,
    listStyle: 'none'   
  }

  const productListItemStyle = {
    margin: '10px 0',
    padding: '5px',
    borderBottom: '1px solid #ccc' 
  }



  return (
    <div>
      <h2>Product List</h2>
      <ul style = {productListStyle}>
        {products.map(product => (
          <li style = {productListItemStyle} key={product.id}>{product.name} - ${product.price}</li>
        ))}
      </ul>
    </div>
  );
  
}

export default ProductList;
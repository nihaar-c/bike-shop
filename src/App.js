import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import ProductList from './ProductList'
import SalesList from './SalesList'
import CustomersList from './CustomerList';


function App() {


  const [showProducts, setShowProducts] = useState(false);
  const displayProducts = () => {
    setShowProducts(!showProducts);
  }

  const [showSales, setShowSales] = useState(false);
  const displaySales = () => {
    setShowSales(!showSales);
  }

  const [showCustomers, setShowCustomers] = useState(false);
  const displayCustomers = () => {
    setShowCustomers(!showCustomers);
  }
  return (
    <div className="App">
      <header className="App-header">
        <button onClick={displayProducts}>
          Display/Hide Products
        </button>
        {showProducts && <ProductList />}

        <button onClick = {displaySales}>
          Display/Hide Sales
        </button>
        {showSales ** <SalesList />}

        <button onClick = {displayCustomers}>
          Display/Hide Customers
        </button>
        {showCustomers ** <CustomersList />}
      </header>
    </div>
  );
}

export default App;

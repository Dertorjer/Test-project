// src/pages/HomePage.js
import React from 'react';

function HomePage() {
    return (
        <div className="home-page">
            <h1>Welcome to HR System</h1>
            <p>This is a simple home page for the HR application.</p>
            <button onClick={() => window.location.href = '/employee-list'}>
                Employee List
            </button>
            <button onClick={() => window.location.href = '/salary-calculator'}>
                Salary Calculator
            </button>
        </div>
    );
}


export default HomePage;

import React, { useState, useMemo } from 'react';
import { Car, Phone, Search, Calendar, Info } from 'lucide-react';

// --- Mock Data ---
const MOCK_CARS = [
  { id: 1, name: 'Model S Plaid', type: 'Sedan', year: 2024, price: 129990, miles: 50, color: 'Red', engine: 'Electric', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Tesla+S' },
  { id: 2, name: 'Ford F-150 Raptor', type: 'Truck', year: 2023, price: 78500, miles: 12000, color: 'Blue', engine: 'V6 EcoBoost', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Ford+Raptor' },
  { id: 3, name: 'Porsche 911 GT3', type: 'Coupe', year: 2022, price: 195000, miles: 500, color: 'Yellow', engine: 'Flat-Six', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Porsche+911' },
];

// --- Shared Components (Required for the Page Layout) ---

// Button component for primary actions
const PrimaryButton = ({ children, onClick, icon: Icon }) => (
  <button
    onClick={onClick}
    className="flex items-center justify-center space-x-2 px-6 py-3 bg-indigo-600 text-white font-semibold rounded-xl shadow-lg hover:bg-indigo-700 transition duration-300 transform hover:scale-[1.02] active:scale-[0.98] focus:outline-none focus:ring-4 focus:ring-indigo-500 focus:ring-opacity-50 min-w-[200px]"
  >
    {Icon && <Icon className="w-5 h-5" />}
    <span>{children}</span>
  </button>
);

// Card component for featured vehicles
// Note: Navigation functions are mocked here since this is a standalone file
const CarCard = ({ car, onClick }) => (
  <div
    className="bg-white rounded-xl shadow-2xl overflow-hidden cursor-pointer transform transition duration-300 hover:shadow-indigo-500/50 hover:scale-[1.02] w-full"
    onClick={() => onClick(car.id)}
  >
    <img
      src={car.image}
      alt={car.name}
      className="w-full h-48 object-cover object-center"
      onError={(e) => {
        e.target.onerror = null;
        e.target.src = `https://placehold.co/600x400/1e293b/ffffff?text=${car.name.replace(/\s/g, '+')}`;
      }}
    />
    <div className="p-4">
      <h3 className="text-xl font-bold text-gray-900 truncate">{car.name}</h3>
      <p className="text-sm text-gray-500 mt-1">
        {car.year} | {car.type}
      </p>
      <div className="mt-3 flex items-center justify-between">
        <span className="text-2xl font-extrabold text-indigo-600">
          ${car.price.toLocaleString()}
        </span>
        <button
          onClick={(e) => {
            e.stopPropagation();
            onClick(car.id);
          }}
          className="text-indigo-600 hover:text-indigo-800 font-medium text-sm transition duration-150"
        >
          View Details &rarr;
        </button>
      </div>
    </div>
  </div>
);

// --- Layout Components ---

const Header = ({ navigate }) => (
  <header className="sticky top-0 z-50 bg-white shadow-lg backdrop-blur-md bg-opacity-90">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center py-4 md:justify-start md:space-x-10">
        <div className="flex justify-start lg:w-0 lg:flex-1">
          <a href="#" onClick={() => navigate('Home')} className="flex items-center">
            <Car className="h-8 w-8 text-indigo-600" />
            <span className="ml-2 text-2xl font-extrabold text-gray-900 tracking-tight">
              {'{company name}'}
            </span>
          </a>
        </div>
        <nav className="hidden md:flex space-x-10">
          {[
            { name: 'Home', page: 'Home' },
            { name: 'About Us', page: 'About' },
            { name: 'Services', page: 'Services' },
            { name: 'Inventory', page: 'Inventory' },
            { name: 'Contact', page: 'Contact' },
          ].map((item) => (
            <a
              key={item.name}
              href={`#${item.page}`}
              onClick={() => navigate(item.page)}
              className="text-base font-medium text-gray-500 hover:text-indigo-600 transition duration-150"
            >
              {item.name}
            </a>
          ))}
        </nav>
        <div className="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <PrimaryButton onClick={() => navigate('Contact')} icon={Phone}>
            Call Us
          </PrimaryButton>
        </div>
      </div>
    </div>
  </header>
);

const Footer = () => (
  <footer className="bg-gray-900 mt-12">
    <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col md:flex-row justify-between items-center text-center md:text-left">
        <div className="mb-4 md:mb-0">
          <p className="text-sm text-gray-400">
            &copy; Christopher Torres, 2025 | {'{company name}'}. All rights reserved.
          </p>
        </div>
        <div className="flex space-x-6">
          <a
            href="#"
            className="text-sm text-gray-400 hover:text-white transition duration-150"
          >
            Terms of Service
          </a>
          <a
            href="#"
            className="text-sm text-gray-400 hover:text-white transition duration-150"
          >
            Privacy Statement
          </a>
        </div>
      </div>
    </div>
  </footer>
);

// --- Home Page Component (Page 1) ---
// Note: navigate and setSelectedCarId are mocked functions here for standalone testing
const HomePage = ({ navigate, setSelectedCarId }) => (
  <main>
    {/* Hero Section (Car image background from PDF) */}
    <div
      className="relative bg-cover bg-center h-[60vh] flex items-center justify-center rounded-b-[4rem] shadow-2xl"
      style={{
        backgroundImage:
          "url('https://placehold.co/1200x800/22223b/ffffff?text=Car+Image+Background')",
      }}
    >
      <div className="absolute inset-0 bg-gray-900 opacity-60 rounded-b-[4rem]"></div>
      <div className="relative text-center p-6 space-y-6">
        <h1 className="text-4xl sm:text-6xl font-extrabold text-white leading-tight">
          Find Your Perfect Drive
        </h1>
        <p className="text-lg text-gray-200 max-w-xl mx-auto">
          Explore our hand-picked inventory of quality new and pre-owned vehicles.
        </p>
        <div className="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-6 pt-4">
          <PrimaryButton onClick={() => navigate('Inventory')} icon={Search}>
            Search Vehicles
          </PrimaryButton>
          <PrimaryButton onClick={() => navigate('Contact')} icon={Calendar}>
            Schedule Test Drive
          </PrimaryButton>
        </div>
      </div>
    </div>

    {/* Featured Cars Section (3 Featured Cars from PDF) */}
    <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h2 className="text-4xl font-bold text-gray-900 mb-8 text-center">Featured Cars</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {MOCK_CARS.map((car) => (
          <CarCard key={car.id} car={car} onClick={(id) => {
            setSelectedCarId(id);
            navigate('Details');
          }} />
        ))}
      </div>
    </section>

    {/* About Us Teaser */}
    <section className="bg-gray-50 py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h3 className="text-3xl font-extrabold text-gray-900">
          Committed to Quality and Service
        </h3>
        <p className="mt-4 text-lg text-gray-600">
          Learn more about our mission and why thousands of customers trust {'{company name}'}.
        </p>
        <div className="mt-8">
          <PrimaryButton onClick={() => navigate('About')} icon={Info}>
            About Us
          </PrimaryButton>
        </div>
      </div>
    </section>
  </main>
);

// --- Main App Entry Point (for standalone use) ---
const App = () => {
  // Mock state management and navigation for standalone file
  const navigate = (page) => console.log(`Navigating to: ${page}`);
  const setSelectedCarId = (id) => console.log(`Selected Car ID: ${id}`);

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 font-sans">
      <Header navigate={navigate} />
      <div className="flex-grow">
        <HomePage navigate={navigate} setSelectedCarId={setSelectedCarId} />
      </div>
      <Footer />
    </div>
  );
};

export default App;
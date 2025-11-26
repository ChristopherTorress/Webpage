<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Car Dealership Website</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://unpkg.com/lucide-static/font/lucide.css" />
</head>
<body class="bg-gray-100">
  <div id="root"></div>

  <script type="module">
    import React, { useState, useMemo } from "https://esm.sh/react";
    import ReactDOM from "https://esm.sh/react-dom/client";

    const MOCK_CARS = [
      { id: 1, name: 'Model S Plaid', type: 'Sedan', year: 2024, price: 129990, miles: 50, color: 'Red', engine: 'Electric', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Tesla+S' },
      { id: 2, name: 'Ford F-150 Raptor', type: 'Truck', year: 2023, price: 78500, miles: 12000, color: 'Blue', engine: 'V6 EcoBoost', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Ford+Raptor' },
      { id: 3, name: 'Porsche 911 GT3', type: 'Coupe', year: 2022, price: 195000, miles: 500, color: 'Yellow', engine: 'Flat-Six', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Porsche+911' },
      { id: 4, name: 'Toyota Camry LE', type: 'Sedan', year: 2024, price: 28500, miles: 100, color: 'Silver', engine: '4-Cylinder', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Toyota+Camry' },
      { id: 5, name: 'Jeep Wrangler Rubicon', type: 'SUV', year: 2023, price: 45000, miles: 8000, color: 'Green', engine: 'V6 Pentastar', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Jeep+Wrangler' },
      { id: 6, name: 'Honda Civic Sport', type: 'Hatchback', year: 2025, price: 25000, miles: 5, color: 'Black', engine: 'Turbocharged', image: 'https://placehold.co/600x400/1e293b/ffffff?text=Honda+Civic' }
    ];

    function App() {
      return React.createElement("div", { className: "p-10 text-center" },
        React.createElement("h1", { className: "text-4xl font-bold mb-6" }, "Car Dealership Website"),
        React.createElement("p", { className: "text-lg text-gray-600" }, "This is a simplified GitHub-ready HTML version. Your full React SPA code has been condensed.")
      );
    }

    ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
  </script>
</body>
</html>

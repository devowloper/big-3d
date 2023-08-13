```javascript
let filament_cost_price;
let filament_sale_price;
let gross_profit_margin;
let infill_percentage = 20;

function calculatePrice(filament_weight, filament_type) {
    if (filament_type === "PLA") {
        filament_cost_price = 20; // cost price per kg for PLA
        filament_sale_price = 30; // sale price per kg for PLA
    } else if (filament_type === "PETG") {
        filament_cost_price = 25; // cost price per kg for PETG
        filament_sale_price = 35; // sale price per kg for PETG
    }

    gross_profit_margin = filament_sale_price - filament_cost_price;
    let price = (filament_weight / 1000) * filament_sale_price; // price for the given weight
    let cost = (filament_weight / 1000) * filament_cost_price; // cost for the given weight
    let profit = price - cost;

    return {
        price: price.toFixed(2),
        cost: cost.toFixed(2),
        profit: profit.toFixed(2),
        gross_profit_margin: gross_profit_margin.toFixed(2)
    };
}

function displayPrice(priceData) {
    let priceDisplay = document.getElementById('priceDisplay');
    priceDisplay.innerHTML = `
        <p>Price: $${priceData.price}</p>
        <p>Cost: $${priceData.cost}</p>
        <p>Profit: $${priceData.profit}</p>
        <p>Gross Profit Margin: ${priceData.gross_profit_margin}%</p>
    `;
}

function onFileUploadSuccess(data) {
    let priceData = calculatePrice(data.weight, data.filament_type);
    displayPrice(priceData);
}

document.addEventListener('fileUploadSuccess', function(e) {
    onFileUploadSuccess(e.detail);
});
```
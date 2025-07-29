const ctx = document.getElementById('item_chart');

const data = {
    labels: month,
    datasets: [
    {
        label: 'Monthly Revenue',
        data: rev_data,
        type: 'line',
        borderColor: "black",
        yAxisID: 'y'
    },
    {
        label: 'Montly Count',
        data: count,
        type: 'bar',
        backgroundColor: 'rgba(131, 131, 131, 0.5)',
        yAxisID: 'y2'

    }]
}

const config = {
    data: data,
    options: {
        scales:{
            y: {
                position: 'left',
                title: {
                    display: true,
                    text: 'Revenue',
                    
                },
                color: 'black'
            },
            y2: {
                position: 'right',
                title: {
                    display: true,
                    text: 'Count'
                }
            }
        }
    }
};
new Chart(ctx, config)
axios.get('/api/v1/statistics/active-user-per-day')
  .then(function (response) {
    let xdata_user=[];
    let ydata_user=[];
    response.data.data.forEach(element => {xdata_user.push(element.day);ydata_user.push(element.count);});
    var chartDom = document.getElementById('active_user');
    var myChart = echarts.init(chartDom,"dark");
    var option;
    
    option = {
        title: {
            text: '1日ごとのユーザー数'
          },
      xAxis: {
        type: 'category',
        data: xdata_user
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: ydata_user,
          type: 'bar'
        }
      ]
    };
    
    myChart.setOption(option);
});


axios.get('/api/v1/statistics/active-room-per-day')
  .then(function (response) {
    let xdata_room=[];
    let ydata_room=[];
    response.data.data.forEach(element => {xdata_room.push(element.day);ydata_room.push(element.count);});
    var chartDom = document.getElementById('active_room');
    var myChart = echarts.init(chartDom,"dark");
    var option;
    
    option = {
        title: {
            text: '1日ごとのルーム数'
          },
      xAxis: {
        type: 'category',
        data: xdata_room
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: ydata_room,
          type: 'bar'
        }
      ]
    };
    
    myChart.setOption(option);
})
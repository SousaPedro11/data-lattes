function vis1(data){
    const MARGIN = { LEFT: 100, RIGHT: 10, TOP: 10, BOTTOM: 130 }
    const WIDTH = 600 - MARGIN.LEFT - MARGIN.RIGHT
    const HEIGHT = 400 - MARGIN.TOP - MARGIN.BOTTOM

    const svg = d3.select("#container-vis1").append("svg")
        .attr("width", WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
        .attr("height", HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)

    const g = svg.append("g")
        .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`)

    // X label
    g.append("text")
        .attr("class", "x axis-label")
        .attr("x", WIDTH / 2)
        .attr("y", HEIGHT + 60)
        .attr("font-size", "20px")
        .attr("text-anchor", "middle")
        .text("Artigos Publicados Ao Longo Dos Anos")

    // Y label
    g.append("text")
        .attr("class", "y axis-label")
        .attr("x", - (HEIGHT / 2))
        .attr("y", -60)
        .attr("font-size", "20px")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .text("Quantidade")

    //app/static/data/articles_dataframe.csv
    //app/templates/articles_dataframe.csv


    const x = d3.scaleBand()
        .domain(data.map(d => d.Ano))
        .range([0, WIDTH])
        .paddingInner(0.3)
        .paddingOuter(0.2)

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.Quantidade)])
        .range([HEIGHT, 0])

    const xAxisCall = d3.axisBottom(x)
    g.append("g")
        .attr("class", "x axis")
        .attr("transform", `translate(0, ${HEIGHT})`)
        .call(xAxisCall)
        .selectAll("text")
        .attr("y", "10")
        .attr("x", "-5")
        .attr("text-anchor", "end")
        .attr("transform", "rotate(-40)")

    const yAxisCall = d3.axisLeft(y)
        .ticks(10)
        .tickFormat(d => d)
    g.append("g")
        .attr("class", "y axis")
        .call(yAxisCall)

    const rects = g.selectAll("rect")
        .data(data)

    rects.enter().append("rect")
        .attr("y", d => y(d.Quantidade))
        .attr("x", (d) => x(d.Ano))
        .attr("width", x.bandwidth)
        .attr("height", d => HEIGHT - y(d.Quantidade))
        .attr("fill", "grey")
    }

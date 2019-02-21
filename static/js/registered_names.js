
console.log('I am here!')



d3.select("#registered_list").append("div")
.attr("class","col-xs-12  col-md-12")  
.append("div")
.attr('id',"people_list")

// url={{ url_for('static',filename='./registered_names.csv')}}

d3.csv("./registered_names.csv", function(error, tvData) {
   if (error) return console.warn(error);
 
   console.log(tvData);
}
)




// d3.json(`/registered_people`,function(error, data) {

//    if (error) return console.warn(error);

//    console.log("data",data)
//    console.log("12345567")
//   console.log("first name",data["first_name"]) 
//   console.log("last name",data["last_name"]) 

// })
//  var table = d3.select("#people_list")
//     .append('div').attr("class","col-md-12").append('div')
//      .attr("id","table-area")
//      .style("text-align", "center")
//      .append('table')
//      .attr('class','table-striped')
//      .style("width","100%")

// var thead=table.append('thead')

// thead.append('th')
// .style("min-width","90px")
// .text("first name ");

// thead.append('th')
// .style("min-width","190px")
// .text("last name");

// tbody=table.append('tbody');
// row=tbody.append('tr')
// row.append('td').text(person.first_name)
// row.append('td').text(person.first_name)

    
// }

// )

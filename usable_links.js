// Link to class website
document.getElementsByClassName("Mrphs-sitesNav__menuitem")[3].getElementsByTagName("a")[0].href

// Get specific tab
document.getElementsByClassName("Mrphs-toolsNav__menu")[0].getElementsByTagName("li")[1]

// Get link to that tab
document.getElementsByClassName("Mrphs-toolsNav__menu")[0].getElementsByTagName("li")[1].children[0].href

// Get table containing class links
document.getElementsByClassName("ant-table-tbody")[0]

// Do not handle pagination: assume student logs into portal at least on the days the class is due, so links will keep getting updated

// Get individual class entries
document.getElementsByClassName("ant-table-tbody")[0].getElementsByClassName("ant-table-row")

// Get link to meeting
document.getElementsByClassName("ant-table-tbody")[0].getElementsByClassName("ant-table-row")[0].children[3].getElementsByClassName("ant-btn")[0].href

// Angular.JS calendar : https://github.com/russiann/flex-calendar

// Get list of assignments
document.getElementsByClassName("table-striped")[0].tBodies[0].rows

// Assignment done?
document.getElementsByClassName("table-striped")[0].tBodies[0].rows[1].children[2].innerText

// deadline
document.getElementsByClassName("table-striped")[0].tBodies[0].rows[1].children[4].innerText

// link to deadline
document.getElementsByClassName("table-striped")[0].tBodies[0].rows[1].children[1].children[0].children[1].href

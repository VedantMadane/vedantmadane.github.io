const app = Vue.createApp({
  el: "#curriculum-vitae",
  data() {
    return {
      searchInput: "",
      dataColumns: ["certification", "date", "institution", "percentage"],
      dataset:  [
        {
          certification: "Bachelor of Engineering in Electronics & Telecommunication", 
          date: "15th June, 2021",
          institution: "University of Mumbai",
          percentage: 62.05},

        {certification: 'Android app using Kotlin', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 72.5},
        {certification: 'Java', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'Arduino', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 75},
        {certification: 'PHP and MySQL', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 61.1},

        { certification: "BE 8th Semester's 2nd Internal Assessment",
        date: "6th May, 2021", institution: "SAKEC", percentage: 82.5},

        {certification: 'Python 3.4.3', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 85},
        {certification: 'Linux', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'RDBMS PostgreSQL', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 57.5},
        {certification: 'C++', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'Java', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 57.5},
        
        { certification: "Spoken Sanskrit Course", date: "13th Aug, 2020",
          institution: "SankritBharati, IIT Roorkee", percentage: 76.25
        },
        {
          certification: "Diploma in Russian Language (536 hour practical course)",date: "31st May, 2019",
          institution: "Pushkin Institute, Moscow, Russia", percentage: 89.5
        },

        {certification: "Higher Secondary Certificate (12th)", date: 2015,
        institution: "Kirti M. Doongursee College, Dadar West", percentage: 69.38
        },
       {certification: "Secondary School Certificate (10th)", date: 2013,
        institution: "St Stanislaus’ High School, Bandra West",      
        percentage: 86.2
       },
      ]
    }
  }
}) 
 
app.component("curriculum-vitae-component", {
  template: "#grid-template",
  props: {
    entries: Array,
    columns: Array,
    filterKey: String
  },
  data: function() {
    return {
      sortKey: ""
    }
  },
  computed: {
    filteredTitles: function() {
      const sortKey = this.sortKey
      
      const filterKey = this.filterKey && this.filterKey.toLowerCase()

      const order = this.sortColumns[sortKey] || 1

      let entries = this.entries

      if (filterKey) {
        entries = entries.filter(function(row) {
          return Object.keys(row).some(function(key) {
            return (
              String(row[key])
              .toLowerCase()
              .indexOf(filterKey) > -1
            )
          })
        })
      }
      if (sortKey) {
        entries = entries.slice().sort(function(x, y) {
          x = x[sortKey]
          y = y[sortKey]
          return (x === y ? 0 : x > y ? 1 : -1) * order
        })
      }
      return entries
    },
      sortColumns() {
        const sortedColumns = {}

        this.columns.forEach(function(key) {
          sortedColumns[key] = 1
        })

        return sortedColumns
      }
    },
    methods: {
      capitalize(inputString) {
        return inputString.charAt(0).toUpperCase() + inputString.slice(1)
      },
      sortBy(key) {
        this.sortKey = key
        this.sortColumns[key] = this.sortColumns[key] * -1
      }
    }
  })

app.mount("#curriculum-vitae")

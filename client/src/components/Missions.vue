<template>
  <div id="missions">
    <v-layout row justify-center>
      <v-dialog v-model="buildLandmarkDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Confirm Placement</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <span>Are you sure you want to permanently place a Landmark here?</span> <br> <br>
            {{newLandmarkLat}}, {{newLandmarkLng}}
            <v-spacer></v-spacer>
          </v-card-text>
          <v-card-actions>
            <v-btn color="red" flat @click.stop="buildLandmarkCancel">Cancel</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" class="light-green" flat @click="placeLandmark">Confirm</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-dialog v-model="buildTowerDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Confirm Placement</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <span>Are you sure you want to permanently place a Tower here?</span> <br> <br>
            {{newTowerLat}}, {{newTowerLng}}
            <v-spacer></v-spacer>
          </v-card-text>
          <v-card-actions>
            <v-btn color="red" flat @click.stop="buildTowerCancel">Cancel</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" class="light-green" flat @click="placeTower">Confirm</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-dialog v-model="missionUnableDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Not enough Experience</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <img
              :src="currentMissionIcon" 
              width=auto
              height=100
            >
            <div v-if="missionDifficulty==='easy'">
              <span>This Mission is <b> <font color="green">easy</font></b> </span>
            </div>
            <div v-if="missionDifficulty==='medium'">
              <span>This Mission is <b> <font color="orange">medium</font></b> </span>
            </div>
            <div v-if="missionDifficulty==='hard'">
              <span>This Mission is <b> <font color="OrangeRed">hard</font></b> </span>
            </div> <br> <br>
            <span>You cannot solve this mission, yet!</span> <br>
            <span>Solve easier Missions before attempting this one</span>
            <v-spacer></v-spacer>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="primary" flat @click.stop="missionUnableDialog=false">Ok</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-dialog v-model="missionBriefing" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Mission Briefing</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <span>You selected the following Mission: </span> <br>
            <strong> {{missionType}} </strong> <br> <br>
            <img
              :src="currentMissionIcon" 
              width=auto
              height=100
            >
            <div v-if="missionDifficulty==='easy'">
              <span>This Mission is <b> <font color="green">easy</font></b> </span>
            </div>
            <div v-if="missionDifficulty==='medium'">
              <span>This Mission is <b> <font color="orange">medium</font></b> </span>
            </div>
            <div v-if="missionDifficulty==='hard'">
              <span>This Mission is <b> <font color="OrangeRed">hard</font></b> </span>
            </div>
            <v-spacer></v-spacer>
            <div v-if=missionRewardsReduced>
              <br> <br>
              <b> Be aware! </b> It is recommended that you solve easier Missions first. <br>
              You will receive <b>reduced Rewards</b> for this Mission if you chose to solve it now.
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" flat @click.stop="missionBriefing=false">Not now</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" dark class="light-green" flat @click.stop="openMission">Solve!</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="submitMissionDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Solve this Mission</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            {{missionQuestion}}
            <div v-if="missionPossibleAnswers == 0">
              <v-text-field label="Your answer" outline v-model="missionAnswer"></v-text-field>
            </div>
            <div v-if="missionPossibleAnswers.length > 0">
              <v-select
                :items="missionPossibleAnswers"
                label="Choose from..."
                v-model="missionAnswer"
              ></v-select>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" flat @click.stop="submitMissionDialog=false">Close</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" dark class="light-green" flat @click="submitMission">Submit</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="missionRewardDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Mission Reward</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            Thank you for solving this mission!
            You have been rewarded with: <br> <br>
            + <b>{{missionKoinReward}} Koins </b><br>
            + <b>{{missionExperienceReward}} Experience </b><br>
            <div v-if=missionRewardsReduced>
              <br>
              <b> (Reduced Rewards) </b>
            </div>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="primary" dark class="light-green" flat @click="closeReward">Ok</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
    <div id='map'>
      
    </div>
    <v-alert class="errorClass"
        v-model="LocationError"
        type="error"
        dismissible
      >
        Error getting location. Please allow location service.
      </v-alert>
      <v-alert class="errorClass"
        v-model="LoginError"
        type="info"
        dismissible
      >
        Please Login or create a new account to start solving Missions
      </v-alert>
  </div>
</template>

<script>
import UserAttributesService from '@/services/UserAttributesService'
import MissionService from '@/services/MissionService'
import TowerService from '@/services/TowerService'
import LandmarkService from '@/services/LandmarkService'

var startPoint = [46.714267, 8.222516];
var mapZoom = 8;
const attributionForMap = '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &vert; <a href="https://github.com/CartoDB/CartoDB-basemaps/blob/master/LICENSE.txt">Map CC-BY</a> &vert; <a href="https://opendatacommons.org/licenses/odbl/">Data ODbL </a> &vert; v1.7'
const tileLayerURL = "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"


var geolocationOptions = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0
};

// Mission Briefing and solving Mission
var currentMissionDetails = ''
var newTower
var newLandmark
var myAttributes

// Leaflet Buttons
var PlaceTowerButton
var PlaceLandmarkButton

export default {
  data() {
    return {
      // current Mission Icon for Briefing
      currentMissionIcon: '',

      // zoomcontrol
      previousZoom: 0,
      zoomedInForBuild: 13,
      // current Level
      myCurrentLevel: 0,
      missionRewardsReduced: false,

      // Leaflet map images
      towerImage: require('@/assets/tower.png'),
      landmarkImage: require('@/assets/landmark.png'),
      visionRangeImage: require('@/assets/vrangeimage.png'),

      missingMaxSpeedImage: require('@/assets/map_icons/missingmaxspeed.svg'),
      missingRoadImage: require('@/assets/map_icons/missingroad.svg'),
      missingPoiImage: require('@/assets/map_icons/missingpoi.svg'),
      missingReligionImage: require('@/assets/map_icons/missingreligion.svg'),
      missingLanguageImage: require('@/assets/map_icons/missinglanguage.svg'),

      // Location Error
      LocationError: false,
      // Login Error
      LoginError: false,

      // Mission Dialog Boxes
      submitMissionDialog: false,
      missionBriefing: false,
      missionRewardDialog: false,
      buildTowerDialog: false,
      buildLandmarkDialog: false,
      missionUnableDialog: false,

      newTowerLat: 0,
      newTowerLng: 0,

      newLandmarkLat: 0,
      newLandmarkLng: 0,
      
      missionQuestion: '',
      missionType: '',
      missionPossibleAnswers: '',
      missionOsmID: '',
      missionDifficulty: '',

      missionKoinReward: 20,
      missionExperienceReward: 10,

      missionAnswer: "",
      title: 'KortMissionMap',
      zoom: 13,
      center: [51.505, -0.09],

      saveDialog: false,
      updateDialogBox: false,
      notifications: false,
      sound: true,
      widgets: false,
    }
  },
  methods: {
    // This Function sends a created Landmark to the backend, updates the UserAttributes and redraws all Landmarks
    async placeLandmark() {
      myAttributes = (await UserAttributesService.getUserAttributes()).data[0]
      
      // Create the tower on the backend
      await LandmarkService.newLandmark(newLandmark)

      // Update the UserAttributes
      myAttributes.landmarks = parseInt(myAttributes.landmarks) - 1
      UserAttributesService.updateUserAttributes(
        {
        'landmarks': myAttributes.landmarks,
        },
        myAttributes.id,
      )
      .then( () => {
        this.buildLandmarkDialog = false
        var self = this
        self.$emit("reloadLandmarks");
      })
    },
    // This Function sends a created tower to the backend, updates the UserAttributes and redraws all missions from all towers
    async placeTower() {
      myAttributes = (await UserAttributesService.getUserAttributes()).data[0]
      // Create the tower on the backend
      await TowerService.newTower(newTower)

      // Update the UserAttributes
      myAttributes.towers = parseInt(myAttributes.towers) - 1
      UserAttributesService.updateUserAttributes(
        {
        'towers': myAttributes.towers,
        },
        myAttributes.id,
      )
      .then( () => {
        this.buildTowerDialog = false
        var self = this
        self.$emit("reloadTowers");
      })
    },
    // This Function cancels placement of a tower
    async buildTowerCancel() {
      this.buildTowerDialog=false
      this.$emit("cancelPlacement");
    },
    // This Function cancels placement of a landmark
    async buildLandmarkCancel() {
      this.buildLandmarkDialog=false
      this.$emit("cancelPlacement");
    },
    // This Function closes the Mission Briefing and opens the Mission Dialog
    openMission() {
      this.missionBriefing = false
      this.submitMissionDialog = true
    },
    // This Function submits a solved Mission to the server and closes the Mission dialog
    submitMission() {
      var solvedMission = {
        "answer": this.missionAnswer,
        "osmID": this.missionOsmID,
        "solved_by": this.$store.state.user,
        "timestamp": Math.floor(new Date().getTime() / 1000)
      }
      var self = this;
      MissionService.postMission(solvedMission)
      .then( (response) => {
        this.submitMissionDialog = false;
        self.$emit("updateSolvedMissions");
        this.missionRewardDialog = true;
        self.$emit("reloadTowers");
        self.$emit("reloadNearbyMissions");
      });
    },
    // This Function closes the reward dialog box that opens after solving a mission
    async closeReward() {
      var self = this;
      this.missionRewardDialog = false
      this.missionOsmID = ''
      this.missionAnswer = ''
      
      //get current Attributes from profile
      myAttributes = (await UserAttributesService.getUserAttributes()).data[0]
      myAttributes.experience = parseInt(myAttributes.experience) + parseInt(this.missionExperienceReward)
      myAttributes.koins = parseInt(myAttributes.koins) + parseInt(this.missionKoinReward)

      UserAttributesService.updateUserAttributes(
        {
        'koins': myAttributes.koins,
        'experience': myAttributes.experience,
        'towers': myAttributes.towers,
        },
        myAttributes.id,
      )
    },
  },
  // This code is executed when the Missions.vue is mounted on the page
  async mounted() {
    var mySolvedMissions
    // make closure of "this"
    var self = this;
    
    if (this.$store.state.isUserLoggedIn) {
      myAttributes = (await UserAttributesService.getUserAttributes()).data[0]
    } else {
      console.log('Player is not logged in')
      self.LoginError=true
    }

    //Show my location on map
    var currentLatitude
    var currentLongitude

    // Layer Groups for all map items
    var CircleGroup = L.layerGroup();
    var currentLocationGroup = L.layerGroup();
    var TowerMissionGroup = L.layerGroup();
    var LeafletTowersIconsGroup = L.layerGroup();
    var LeafletLandmarksIconsGroup = L.layerGroup();
    var locationErrorOnce = true;


    navigator.geolocation.getCurrentPosition(geoLocationSuccess, geoLocationError, geolocationOptions);
    
    async function geoLocationSuccess(pos) {
      var crd = pos.coords;

      //Draws the circle
      CircleGroup.clearLayers();
      var visionLat = crd.latitude
      var visionLon = crd.longitude
      var visionRangeIcon = L.icon({
          iconUrl:      self.visionRangeImage,
          iconSize:     [35, 35], // size of the icon
          iconAnchor:   [17, 17], // point of the icon which will correspond to marker's location
          shadowAnchor: [17, 35],  // the same for the shadow
          popupAnchor:  [0, -17] // point from which the popup should open relative to the iconAnchor
      });
      L.marker([visionLat, visionLon], {icon: visionRangeIcon}).addTo(CircleGroup)
      if (self.$store.state.isUserLoggedIn) {
        L.circle([visionLat, visionLon], {radius: myAttributes.sight_range, color:'blue',opacity:0.08,fillColor: 'blue',fillOpacity:.0}).addTo(CircleGroup);
      }else{
        L.circle([visionLat, visionLon], {radius: 2000, color:'blue',opacity:0.08,fillColor: 'blue',fillOpacity:.0}).addTo(CircleGroup);
      }
      CircleGroup.addTo(map)

      currentLatitude = crd.latitude
      currentLongitude = crd.longitude

      setTimeout(function(){ navigator.geolocation.getCurrentPosition(geoLocationSuccess, geoLocationError, geolocationOptions); }, 10000);
      getNearbyMissions()
    }  

    function geoLocationError(err) {
      console.warn(`ERROR(${err.code}): ${err.message}`);
      setTimeout(function(){ navigator.geolocation.getCurrentPosition(geoLocationSuccess, geoLocationError, geolocationOptions); }, 10000);
      console.log("gettingLocationError");
      if (locationErrorOnce) {
        self.LocationError = true
        locationErrorOnce = false
      }
    }

    if (this.$store.state.mapPos != null) {
      startPoint = [self.$store.state.mapPos.lat, self.$store.state.mapPos.lng]
    }
    if (this.$store.state.mapZoom != null) {
      mapZoom = self.$store.state.mapZoom
    }
    // init the map object
    var map = L.map('map', {attributionControl: false}).setView(startPoint, mapZoom),
      tilelayer = L.tileLayer(tileLayerURL, {
        attribution: attributionForMap,
        minZoom: 5,
        maxZoom: 18,
        ext: 'png',
      }).addTo(map);

    // remove the "Leaflet" attribution prefix
    var myAttribution = L.control.attribution({prefix: '', position: 'bottomright'}).addTo(map);

    map.on('zoomend', function() {
      self.$store.dispatch('saveMapPos', map.getCenter())
      self.$store.dispatch('saveMapZoom', map.getZoom())
    });

    map.on('dragend', function() {
      self.$store.dispatch('saveMapPos', map.getCenter())
    });

    // This function draws a Landmark on the LeafletLandmarksIconsGroup
    async function placeLandmarkIconOnMap(inLat, inLon, inLabel) {
      var landmarkLat = inLat
      var landmarkLon = inLon
      var landmarkLabel = inLabel
      var landmarkIcon = L.icon({
          iconUrl:      self.landmarkImage,
          iconSize:     [38, 42], // size of the icon
          iconAnchor:   [19, 21], // point of the icon which will correspond to marker's location
          shadowAnchor: [4, 62],  // the same for the shadow
          popupAnchor:  [19, -20] // point from which the popup should open relative to the iconAnchor
      });
      //L.marker([towerLat, towerLon], {icon: landmarkIcon}).addTo(LeafletLandmarksIconsGroup);
      L.marker([landmarkLat, landmarkLon], {icon: landmarkIcon, name:landmarkLabel}).addTo(map).on('click', clickedLandmark).bindTooltip(landmarkLabel, {direction:'top', permanent:true, offset:[0,-20] }).openTooltip();
    }

    // This function draws a tower on the LeafletTowersIconsGroup
    async function placeTowerIconOnMap(inLat, inLon) {
      var towerLat = inLat
      var towerLon = inLon
      var towerIcon = L.icon({
          iconUrl:      self.towerImage,
          iconSize:     [18, 30], // size of the icon
          iconAnchor:   [9, 15], // point of the icon which will correspond to marker's location
          shadowAnchor: [4, 62],  // the same for the shadow
          popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
      });
      L.circle([towerLat, towerLon], {radius: myAttributes.tower_range, color:'black',opacity:0.1,fillColor: 'black',fillOpacity:0}).addTo(LeafletTowersIconsGroup);
      L.marker([towerLat, towerLon], {icon: towerIcon}).addTo(LeafletTowersIconsGroup);
    }

    // Geolocation and Marker 
    // Here the browser attempts to return a geolocation and asks the user for permission
    map.locate({setView: false, maxZoom: 15, enableHighAccuracy:false, timeout:5000, maximumAge:0});

    // Get all my previously solved Missions
    mySolvedMissions = await getMySolvedMissions()

    // This function updates the List of solved Missions via the eventhub
    this.$on("updateSolvedMissions", async function(){
      mySolvedMissions = await getMySolvedMissions()
    })
    
    // This function retrieves the list of all previously solved Missions by this User from the backend Server
    async function getMySolvedMissions() {
      let myMissions = await MissionService.getSolvedMissions()
      return myMissions.data
    }

    // This function adds all nearby Missions to the map via the eventhub
    this.$on("reloadNearbyMissions", async function(){
      getNearbyMissions()
    })
    // init Icons for map
    var maxSpeedIcon = L.icon({
      iconUrl:      self.missingMaxSpeedImage,
      iconSize:     [30,30],
      iconAnchor:   [15,18]
    });
    var roadIcon = L.icon({
      iconUrl:      self.missingRoadImage,
      iconSize:     [30,30],
      iconAnchor:   [15,17]
    });
    var poiIcon = L.icon({
      iconUrl:      self.missingPoiImage,
      iconSize:     [29,29],
      iconAnchor:   [15,14]
    });
    var religionIcon = L.icon({
      iconUrl:      self.missingReligionImage,
      iconSize:     [30,30],
      iconAnchor:   [15,15]
    });
    var religionIcon = L.icon({
      iconUrl:      self.missingReligionImage,
      iconSize:     [30,30],
      iconAnchor:   [15,15]
    });
    var languageIcon = L.icon({
      iconUrl:      self.missingLanguageImage,
      iconSize:     [30,30],
      iconAnchor:   [15,15]
    });
    
    // Add Missions from current location
    async function getNearbyMissions() {
      var range = 2000
      if (self.$store.state.isUserLoggedIn) {
        //myAttributes = (await UserAttributesService.getUserAttributes()).data[0]
        range = parseInt(myAttributes.sight_range)
      }
      self.$http.get('/api_kort/v1.0/missions?user_id=-1&lat='+currentLatitude+'&lon='+currentLongitude+'&radius='+range+'&limit=100&lang=en', {foo: 'bar'}).then(response => {

      // get status
      response.status;

      // get status text
      response.statusText;

      // get 'Expires' header
      response.headers.get('Expires');

      // get body data
      self.someData = response.body;

      // Draw all nearby Missions from response
      currentLocationGroup.clearLayers();
      self.someData.forEach(k => {
        if (k.error_type  && !checkMissionSolvedStatus(mySolvedMissions, k.osmId)) {
          // Default color blue (unrecognized mission type)
          // Mission Mapping (Difficulty)
          let difficulty = 'hard'
          let strokecolor =  'OrangeRed'
          let missionIcon = roadIcon
          let missionIconImage = self.missingRoadImage
          if (k.error_type == "missing_track_type") {
            strokecolor = 'yellow'
            difficulty = 'medium'
            missionIcon = roadIcon
            missionIconImage = self.missingRoadImage
          }
          if (k.error_type == "missing_maxspeed") {
            strokecolor = 'orange'
            difficulty = 'medium'
            missionIcon = maxSpeedIcon
            missionIconImage = self.missingMaxSpeedImage
          }
          if (k.error_type == "poi_name") {
            strokecolor = 'OrangeRed'
            difficulty = 'hard'
            missionIcon = poiIcon
            missionIconImage = self.missingPoiImage
          }
          if (k.error_type == "language_unknown") {
            strokecolor = 'green'
            difficulty = 'easy'
            missionIcon = languageIcon
            missionIconImage = self.missingLanguageImage
          }
          if (k.error_type == "religion") {
            strokecolor = 'Chartreuse'
            difficulty = 'easy'
            missionIcon = religionIcon
            missionIconImage = self.missingReligionImage
          }
          L.circleMarker([k.annotationCoordinate[0], k.annotationCoordinate[1]], {radius: 6, color:strokecolor, k, difficulty, missionIconImage}).addTo(currentLocationGroup).on('click', clickedMission);
        }
      });
      currentLocationGroup.addTo(map)

    }, response => {
      console.log("getting missions failed")
    });

    }

    // This function is triggered when a Player has clicked a Landmark
    function clickedLandmark(e) {
      console.log('you clicked landmark of: ' + this.options.name)
    }

    // This function is triggered when a Player clicks a mission on the map
    function clickedMission(e) { 
      if (!self.$store.state.isUserLoggedIn) {
        self.LoginError=true
      } else {
        self.submitMissionDialog = false
        //self.missionBriefing = true

        // Mission Icon for Briefing
        self.currentMissionIcon = this.options.missionIconImage

        currentMissionDetails = this.options.k
        self.missionType = currentMissionDetails.title
        self.missionQuestion = currentMissionDetails.question
        self.missionPossibleAnswers = currentMissionDetails.inputType.options
        self.missionOsmID = currentMissionDetails.osmId
        
        self.missionDifficulty = this.options.difficulty

        // fix Missions answer "Asphalt" (Issue #23)
        if (self.missionPossibleAnswers[0] == "Asphalt, concrete or cobblestone") {
          self.missionPossibleAnswers.splice(0,1, "Asphalt")
          self.missionPossibleAnswers.splice(1,0, "Concrete")
          self.missionPossibleAnswers.splice(2,0, "Cobblestone")
        }

        // Todo:
        // mission reward adjustements for difficulty and current level here
        // get Player Level, make adjustements
        var currentPlayerLevel = calculateXPLevel(myAttributes.experience)
        self.myCurrentLevel = currentPlayerLevel
        console.log('myCurrentLevel: ' + currentPlayerLevel)
        console.log('thisMissions Level: ' + self.missionDifficulty)
        
        // default; Player gains full mission rewards for a solved mission (no message shown)
        self.missionRewardsReduced = false

        
        if (self.missionDifficulty == 'easy') {
          self.missionBriefing = true
          self.missionKoinReward = 20
          self.missionExperienceReward = 10
        }

        if (self.missionDifficulty == 'medium') {
          if (currentPlayerLevel < 2) {
            self.missionBriefing = true
            self.missionRewardsReduced = true
            self.missionKoinReward = 5
            self.missionExperienceReward = 5
          } else {
            self.missionBriefing = true
            self.missionKoinReward = 30
            self.missionExperienceReward = 20
          }
        }

        if (self.missionDifficulty == 'hard') {
          if (currentPlayerLevel < 2) {
            self.missionUnableDialog = true
          } else if (currentPlayerLevel < 3) {
            self.missionBriefing = true
            self.missionRewardsReduced = true
            self.missionKoinReward = 5
            self.missionExperienceReward = 5
          } else {
            self.missionBriefing = true
            self.missionKoinReward = 60
            self.missionExperienceReward = 40
          }
        }
      }
    }

    // Helper function to calculate the current Player Level based on their current XP
    // returns Level 1, 2, 3 or higher
    function calculateXPLevel(currentXP) {
      var currentLevel = 0
      if (currentXP < 50 ) {
        currentLevel = 1
      } else if (currentXP < 550 ) {
        currentLevel = 2
      } else if (currentXP < 2330 ) {
        currentLevel = 3
      } else {
        // Default "maxed"
        currentLevel = 4
      }
      return currentLevel
    }

    // Show "place tower" button on map if any Towers are available and user is logged in
    if (self.$store.state.isUserLoggedIn) {
      if (parseInt(myAttributes.towers) >= 1) {
        L.NewTowerControl = L.Control.extend({
          options: {
            position: 'topright'
          },
          onAdd: function(map) {
            var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar');
            var title = L.DomUtil.create('div', 'ControlTitle', container)
            var image = L.DomUtil.create('img', '', container)
            var amount = L.DomUtil.create('div', 'amount', container)
            title.innerHTML = 'Towers'
            title.style.width = '80px';
            title.style.margintop = '10px';
            title.style.fontSize = 'larger';
            amount.innerHTML = myAttributes.towers;
            amount.width = '40px';
            image.src = self.towerImage;
            image.style.width = '40px';
            image.style.height = 'auto';
            container.style.background = 'white';
            L.DomEvent.on(container, 'click', L.DomEvent.stop)
              .on(container, 'click', function() {
                if (parseInt(myAttributes.towers) >= 1) {
                  console.log('placing tower now...')
                  console.log(map.getCenter())
                  newTower = {
                    'location': [map.getCenter().lat.toFixed(5), map.getCenter().lng.toFixed(5)]
                  }
                  // open the Dialogbox before placeing a new tower
                  self.newTowerLat = map.getCenter().lat.toFixed(5)
                  self.newTowerLng = map.getCenter().lng.toFixed(5)
                  // zoom in to build
                  self.previousZoom = map.getZoom()
                  if (map.getZoom() < self.zoomedInForBuild) {
                    map.setZoom(self.zoomedInForBuild)
                  }
                  // open dialog to confirm
                  self.buildTowerDialog = true
                  amount.innerHTML = parseInt(myAttributes.towers) - 1;
                  if (parseInt(myAttributes.towers) == 1) {
                    container.style.display = 'none'
                  }
                } else {
                  console.log('no towers available...')
                  container.style.display = 'none';
                }
              });
            container.style.display = 'block';
            return container;
          }
        });
        PlaceTowerButton = new L.NewTowerControl
        map.addControl(PlaceTowerButton);
      }
    }    

    // Show "place landmark" button on map if any landmarks are available and user is logged in
    if (self.$store.state.isUserLoggedIn) {
      if (myAttributes.landmarks >= 1) {
        L.NewLandmarkControl = L.Control.extend({
          options: {
            position: 'topright'
          },
          onAdd: function(map) {
            var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar');
            var title = L.DomUtil.create('div', 'ControlTitle', container)
            var image = L.DomUtil.create('img', '', container)
            var amount = L.DomUtil.create('div', 'amount', container)
            title.innerHTML = 'Landmarks'
            title.style.width = '80px';
            title.style.margintop = '10px';
            title.style.fontSize = 'larger';
            amount.innerHTML = myAttributes.landmarks;
            amount.width = '40px';
            image.src = self.landmarkImage;
            image.style.width = '40px';
            image.style.height = 'auto';
            container.style.background = 'white';
            L.DomEvent.on(container, 'click', L.DomEvent.stop)
              .on(container, 'click', function() {
                if (parseInt(myAttributes.landmarks) >= 1) {
                  console.log('placing landmark now...')
                  console.log(map.getCenter())
                  newLandmark = {
                    'location': [map.getCenter().lat.toFixed(5), map.getCenter().lng.toFixed(5)],
                    'label': self.$store.state.user,
                    'owner': self.$store.state.user,
                  }
                  // open the Dialogbox before placeing a new landmark
                  self.newLandmarkLat = map.getCenter().lat.toFixed(5)
                  self.newLandmarkLng = map.getCenter().lng.toFixed(5)
                  // zoom in to build
                  self.previousZoom = map.getZoom()
                  if (map.getZoom() < self.zoomedInForBuild) {
                    map.setZoom(self.zoomedInForBuild)
                  }
                  // open dialog to confirm
                  self.buildLandmarkDialog = true
                  amount.innerHTML = parseInt(myAttributes.landmarks) - 1;
                  if (parseInt(myAttributes.landmarks) == 1) {
                    container.style.display = 'none'
                  }
                } else {
                  console.log('no landmarks available...')
                  container.style.display = 'none';
                }
              });
            container.style.display = 'block';
            return container;
          }
        });
        PlaceLandmarkButton = new L.NewLandmarkControl();
        map.addControl(PlaceLandmarkButton);
      }
    }

    // This function is executed if the Player cancels the placement of a Tower from the Dialog
    // All buttons are removed and added in the correct order
    this.$on("cancelPlacement", async function(){
      map.setZoom(self.previousZoom)
      if (parseInt(myAttributes.towers) > 0) {
        map.addControl(PlaceTowerButton);
      }
      if (parseInt(myAttributes.landmarks) > 0) {
        map.addControl(PlaceLandmarkButton);
      }
    })

    // initially draw all available towers
    getAllTowers()

    // This function is called when the eventhub emits the reloadTowers event
    this.$on("reloadTowers", function(){
      getAllTowers();
    })
    
    // This Function retrieves and adds all Missions from all Towers to the map
    async function getAllTowers() {
      var allTowers = await TowerService.getMyTowers()

      TowerMissionGroup.clearLayers();
      LeafletTowersIconsGroup.clearLayers()
      allTowers.data.forEach(t=> {
        if (t.location.length > 0) {
          getMissionsFromTower(t.location[0], t.location[1])
          placeTowerIconOnMap(t.location[0], t.location[1])
        }
      })
      TowerMissionGroup.addTo(map)
      LeafletTowersIconsGroup.addTo(map)
    }

    // initially draw all available landmarks
    getAllLandmarks()

    // This function is called when the eventhub emits the reloadLandmarks event
    this.$on("reloadLandmarks", function(){
      getAllLandmarks();
    })
    
    // This Function retrieves and adds all Missions from all Towers to the map
    async function getAllLandmarks() {
      var allLandmarks = await LandmarkService.getAllLandmarks()

      LeafletLandmarksIconsGroup.clearLayers()
      allLandmarks.data.forEach(t=> {
        if (t.location.length > 0) {
          placeLandmarkIconOnMap(t.location[0], t.location[1], t.label)
        }
      })
      LeafletLandmarksIconsGroup.addTo(map)
    }

    // helper function to check if a mission (osmID) is already solved
    function checkMissionSolvedStatus(arr, val) {
      return arr.some(function(arrVal) {
        return val.toString() === arrVal.osmID;
      });
    }

    // Add Missions from a Tower
    async function getMissionsFromTower(towerLat, towerLng) {
      var range = parseInt(myAttributes.tower_range)
      self.$http.get('/api_kort/v1.0/missions?user_id=-1&lat='+towerLat+'&lon='+towerLng+'&radius='+range+'&limit=100&lang=en', {foo: 'bar'}).then(response => {

      // get status
      response.status;
      // get status text
      response.statusText;
      // get 'Expires' header
      response.headers.get('Expires');
      // get body data
      self.someData = response.body;

      //Add all Missions from response to layerGroup TowerMissionGroup
      self.someData.forEach(k => {
        if (k.error_type && !checkMissionSolvedStatus(mySolvedMissions, k.osmId)) {
          //Default color blue
          //Mission Mapping (Difficulty)
          let difficulty = 'hard'
          let strokecolor =  'OrangeRed'
          let missionIcon = roadIcon
          let missionIconImage = self.missingRoadImage
          if (k.error_type == "missing_track_type") {
            strokecolor = 'yellow'
            difficulty = 'medium'
            missionIcon = roadIcon
            missionIconImage = self.missingRoadImage
          }
          if (k.error_type == "missing_maxspeed") {
            strokecolor = 'orange'
            difficulty = 'medium'
            missionIcon = maxSpeedIcon
            missionIconImage = self.missingMaxSpeedImage
          }
          if (k.error_type == "poi_name") {
            strokecolor = 'OrangeRed'
            difficulty = 'hard'
            missionIcon = poiIcon
            missionIconImage = self.missingPoiImage
          }
          if (k.error_type == "language_unknown") {
            strokecolor = 'green'
            difficulty = 'easy'
            missionIcon = languageIcon
            missionIconImage = self.missingLanguageImage
          }
          if (k.error_type == "religion") {
            strokecolor = 'Chartreuse'
            difficulty = 'easy'
            missionIcon = religionIcon
            missionIconImage = self.missingReligionImage
          }
          //L.marker([k.annotationCoordinate[0], k.annotationCoordinate[1]], {icon: missionIcon, k, difficulty, missionIconImage}).addTo(TowerMissionGroup).on('click', clickedMission);
          L.circleMarker([k.annotationCoordinate[0], k.annotationCoordinate[1]], {radius: 6, color:strokecolor, k, difficulty, missionIconImage}).addTo(TowerMissionGroup).on('click', clickedMission);
        }
      });
    }, response => {
      console.log("getting missions failed")
    });

    } 
  }
}

</script>
<style type='text/css'>

body {
  margin: 0;
  padding: 0;
}

#map {
  position: absolute;
  top: 66px;
  bottom: 0;
  right: 0;
  left: 0;
  width: 100%;
}

.leaflet-sidebar>.leaflet-control {
  overflow-y: hidden;
  text-align: 'center';
}

.leaflet-sidebar>.leaflet-control>.ControlTitle {
  width: '80px';
  background-color: 'red';
  text-align: 'center';
}

div.overlay--active {
  z-index: 1000 !important
}

div.dialog__content__active {
  z-index: 1000 !important
}

div.errorClass {
  z-index: 2000 !important
}

</style>

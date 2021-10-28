/**
 * If you want to look into the code, it's probably easier to look here:
 * https://github.com/callumacrae/animation-talk-demo/blob/main/src/views/SvgAnimation.vue
 * 
 * There's other stuff in the repo, but it's mostly the SVG animation.
 */

import chroma from "https://cdn.skypack.dev/chroma-js@2.1.2";
// gsap being used for state transitions only, not animating!
import { gsap } from "https://cdn.skypack.dev/gsap@3.8.0";
// todo why isn't vue-slider-component working here
import VueSlider from "https://cdn.skypack.dev/vue-slider-component@3.2.15";

const app = Vue.createApp({
  components: { VueSlider },
  setup() {
    const { computed, ref, watch } = Vue;

    const controlSection = ref(0);

    const boatVisible = ref(true);
    const cloudCount = ref(5);
    const time = ref(18);

    const waterColorScale = chroma
      .scale(["aqua", "darkblue", "#000042"])
      .domain([16, 18, 20]);
    const waterColor = computed(() => {
      return waterColorScale(time.value);
    });

    const boatColorScale = chroma.scale(["orange", "#725010"]).domain([18, 20]);
    const boatColor = computed(() => {
      return boatColorScale(time.value);
    });
    // This is simulating opacity, but we don't want to see mountain shadows through
    // the boat so we can't actually use opacity
    const boatShadowColor = computed(() => {
      return chroma.mix(waterColor.value, boatColor.value, 0.2);
    });

    function numToTime(num) {
      const h = Math.floor(num);
      const m = Math.round((num % 1) * 60);
      return `${h}:${m < 10 ? "0" + m : m}`;
    }

    const pageBgScale = chroma
      .scale(["deepskyblue", "#1f2937", "#0c1726"])
      .domain([16, 18, 20]);
    watch(time, (newTime) => {
      document.body.style.backgroundColor = pageBgScale(newTime).hex();
    });
    
    function goToTime(newTime) {
      const duration = Math.abs(newTime - time.value) / 2;
      gsap.to(time, { value: newTime, duration, ease: "sine.inOut" });
    }

    return { controlSection, boatVisible, cloudCount, time, waterColor, boatColor, boatShadowColor, numToTime, goToTime };
  }
});

app.component("Boat", {
  template: "#boat"
});

app.component("Clouds", {
  template: "#clouds",
  props: ["time", "cloudCount"],
  setup(props) {
    const { computed, ref, watch } = Vue;

    const cloudColorScale = chroma
      .scale(["white", "pink", "#4c363a"])
      .domain([12, 18, 20]);
    const cloudColor = computed(() => {
      return cloudColorScale(props.time);
    });

    const clouds = ref([
      { id: 0, x: 134, y: 170, scaleX: 1, scaleY: 1 },
      { id: 1, x: 500, y: 60, scaleX: -1.1, scaleY: 1.1 },
      { id: 2, x: 945, y: 105, scaleX: 1, scaleY: 1 },
      { id: 3, x: 1050, y: 300, scaleX: -1, scaleY: 1 },
      { id: 4, x: 1350, y: 205, scaleX: -1.1, scaleY: 1.2 },
    ]);

    let maxId = 4;

    function addCloud() {
      maxId++;
      clouds.value.push({
        id: maxId,
        x: 100 + Math.random() * 1400,
        y: 30 + Math.random() * 300,
        scaleX: (Math.random() < 0.5 ? -1 : 1) * (0.8 + Math.random() * 0.4),
        scaleY: 0.8 + Math.random() * 0.5,
      });
    }

    function removeCloud() {
      clouds.value.splice(0, 1);
    }

    watch(
      () => props.cloudCount,
      (cloudCount) => {
        if (cloudCount > clouds.value.length) {
          addCloud();
        } else if (cloudCount < clouds.value.length) {
          removeCloud();
        }
      }
    );

    return { cloudColor, clouds };
  }
});

app.component("FgMountains", {
  template: "#fgMountains",
  props: ["time", "rightOnly"],
  setup(props) {
    const { computed } = Vue;

    const bgColorScale = chroma.scale(["darkgreen", "purple", "#1a001a"]).domain([16, 18, 20]);
    const bgColor = computed(() => {
      return bgColorScale(props.time);
    });

    const fgColorScale = chroma.scale(["green", "#520752", "#2c002c"]).domain([16, 18, 20]);
    const fgColor = computed(() => {
      return fgColorScale(props.time);
    });
    
    return { bgColor, fgColor };
  }
});

app.component("Mountains", {
  template: "#mountains",
  props: ["time", "rightOnly"],
  setup(props) {
    const { computed } = Vue;

    const bgColorScale = chroma.scale(["darkgreen", "magenta", "purple"]).domain([16, 18, 20]);
    const bgColor = computed(() => {
      return bgColorScale(props.time);
    });

    const fgColorScale = chroma.scale(["green", "red", "#520752"]).domain([16, 18, 20]);
    const fgColor = computed(() => {
      return fgColorScale(props.time);
    });
    
    return { bgColor, fgColor };
  }
});

app.component("Moon", {
  template: "#moon",
  props: ["time"],
  setup(props) {
    const { computed } = Vue;

    const opacity = computed(() => {
      if (props.time < 19) {
        return 0;
      }

      return props.time - 19;
    });
    
    return { opacity };
  }
});

app.component("Sun", {
  template: "#sun",
  props: ["time"],
  setup(props) {
    const { computed } = Vue;

    const rotation = computed(() => {
      return ((props.time - 14) / 4) * 50 - 50;
    });
    
    return { rotation };
  }
});

app.component("Stars", {
  template: "#stars",
  props: ["time"],
  setup(props) {
    const { computed, ref, onMounted, onUnmounted } = Vue;

    const stars = [];

    for (let i = 0; i < 250; i++) {
      stars.push({
        i: i,
        r: 3 + Math.random() * 2,
        cx: Math.random() * 3200,
        cy: Math.random() * 3200,
        h: Math.random() * 360,
      });
    }

    const opacity = computed(() => {
      if (props.time < 17.5) {
        return 0;
      }
      if (props.time > 19.5) {
        return 1;
      }

      return (props.time - 17.5) / 2;
    });

    const rotation = ref(0);

    let frameId;
    const frame = (time) => {
      frameId = requestAnimationFrame(frame);

      if (props.time < 17) {
        return;
      }

      rotation.value = time / 1e3;
    };
    onMounted(() => {
      frameId = requestAnimationFrame(frame);
    });
    onUnmounted(() => {
      cancelAnimationFrame(frameId);
    });
    
    return { opacity, rotation, stars };
  }
});


app.mount("#app");

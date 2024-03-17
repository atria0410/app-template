import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    // ... your configuration
    defaults: {
      VInput: {
        density: 'compact'
      },
      VTextField: {
        variant: 'outlined',
        density: 'compact'
      },
      VTextarea: {
        variant: 'outlined',
        density: 'compact'
      },
      VSelect: {
        variant: 'outlined',
        density: 'compact'
      },
      VAutocomplete: {
        variant: 'outlined',
        density: 'compact'
      },
      VFileInput: {
        variant: 'outlined',
        density: 'compact',
        prependIcon: '',
        appendInnerIcon: 'mdi-paperclip'
      },
      VCombobox: {
        variant: 'outlined',
        density: 'compact'
      },
      VCheckbox: {
        density: 'compact',
        color: 'primary'
      },
      VSwitch: {
        density: 'compact',
        color: 'primary'
      },
      VRadio: {
        density: 'compact',
        color: 'primary'
      },
      VRadioGroup: {
        density: 'compact',
        color: 'primary'
      },
      VSlider: {
        density: 'compact',
        color: 'primary'
      },
      VRangeSlider: {
        density: 'compact'
      }
    }
  })
  app.vueApp.use(vuetify)
})

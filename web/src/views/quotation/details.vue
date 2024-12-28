<template>
  <div v-if="!props.uuid">
    <n-alert title="Info" type="info">
      Please select a project to see the details.
    </n-alert>
  </div>
  <div v-else-if="loading" class="loading">
    <n-spin size="large" />
  </div>
  <div v-else-if="projectDetails">
    <n-alert title="Success" type="success" closable>
      Project details fetched successfully.
    </n-alert>
    <n-divider>
      <h2>Project Details</h2>
    </n-divider>
    <n-alert>
      <div v-if="qrCodeDataUrl" style="display: flex; align-items: center;">
        <img :src="qrCodeDataUrl" alt="QR Code" style="max-width: 85px;" />
        <div style="margin-left: 10px">
          <p><strong>Project ID:</strong> {{ props.uuid }}</p>
          <p><strong>Client:</strong> {{ projectDetails.client }}</p>
          <p><strong>Due Date:</strong> {{ projectDetails.due }}</p>
        </div>
      </div>
    </n-alert>
    <n-alert :show-icon="false" type="info">
      <Progress />
    </n-alert>
    <p><strong>Project Name:</strong> {{ projectDetails.name }}</p>
    <p><strong>Client:</strong> {{ projectDetails.client }}</p>
    <p><strong>Status:</strong> {{ projectDetails.status }}</p>
    <p><strong>Start Date:</strong> {{ projectDetails.startDate }}</p>
    <p><strong>End Date:</strong> {{ projectDetails.endDate }}</p>
    <p><strong>Description:</strong> {{ projectDetails.description }}</p>

  </div>
  <div v-else>
    <n-alert title="Error" type="error">
      Failed to fetch project details.
    </n-alert>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import api from '@/api'
import { defineProps } from 'vue'
import { NSpin, NAlert } from 'naive-ui'
import Progress from './progress.vue'
import QRCode from 'qrcode'

const props = defineProps({
  uuid: String,
})

const projectDetails = ref(null)
const loading = ref(false)
const qrCodeDataUrl = ref('')

watch(
  () => props.uuid,
  async (newUuid) => {
    if (newUuid) {
      loading.value = true
      try {
        const response = await api.getProjectDetails(newUuid)
        projectDetails.value = response.data[0]
        qrCodeDataUrl.value = await QRCode.toDataURL(newUuid)
      } catch (error) {
        console.error('Failed to fetch project details:', error)
      } finally {
        loading.value = false
      }
    }
  }
)
</script>

<style scoped>
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.n-alert:not(:last-child) {
  margin-bottom: 12px;
}
.n-card {
  margin-bottom: 12px;
}
</style>
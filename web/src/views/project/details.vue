<template>
  <div v-if="!props.uuid">
    <n-alert title="Info" type="info"> Please select a project to see the details. </n-alert>
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
      <div v-if="qrCodeDataUrl" style="display: flex; align-items: center">
        <img :src="qrCodeDataUrl" alt="QR Code" style="max-width: 85px" />
        <div style="margin-left: 10px">
          <p><strong>Active:</strong> {{ projectDetails.active }}</p>
          <p><strong>Job ID:</strong> {{ projectDetails.job_id }}</p>
          <p><strong>Client:</strong> {{ projectDetails.client }}</p>
          <p><strong>Due Date:</strong> {{ projectDetails.due_date }}</p>
        </div>
      </div>
    </n-alert>
    <n-alert :show-icon="false" type="info">
      <Progress :status="projectDetails.status" />
    </n-alert>
    <n-divider>
      <h2>Client Info</h2>
    </n-divider>
    <div class="client">
      <p>
        Client: <strong>{{ projectDetails.client }}</strong>
      </p>
      <p>
        Contact Person: <strong>{{ projectDetails.contact_person }}</strong>
      </p>
      <p>
        Contact Method:
        <span v-for="(method, index) in parsedContactMethods" :key="index">
          <n-tag type="success" style="margin-left: 5px">{{ method }}</n-tag>
        </span>
      </p>
      <p>
        Contact Details: <strong>{{ projectDetails.contact_details }}</strong>
      </p>
    </div>
    <n-divider>
      <h2>Quotation Info</h2>
    </n-divider>

  </div>
  <div v-else>
    <n-alert title="Error" type="error"> Failed to fetch project details. </n-alert>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
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

const parsedContactMethods = computed(() => {
  if (!projectDetails.value || !projectDetails.value.contact_method) return []
  try {
    return projectDetails.value.contact_method.slice(1, -1).split(',').map(method => method.trim())
  } catch (error) {
    console.error('Failed to parse contact methods:', error)
    return []
  }
})

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
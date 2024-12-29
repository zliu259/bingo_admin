<template>
  <n-split direction="horizontal" style="height: 100%" max="1200px" min="800px">
    <template #1>
      <n-scrollbar style="max-height: 100%">
        <div class="operation-section">
          <n-button strong secondary round type="primary" @click="showModal = true">Create</n-button>
        </div>
        <div class="table-section">
          <Table @show-details="handleShowDetails" />
        </div>
      </n-scrollbar>
    </template>
    <template #2>
      <n-scrollbar style="max-height: 100%">
        <div class="form-section">
          <Details :uuid="selectedUuid" />
        </div>
      </n-scrollbar>
    </template>
  </n-split>

  <n-modal v-model:show="showModal" title="Create New Project">
    <n-form @submit.prevent="handleSubmit">
      <n-form-item label="Project Name">
        <n-input v-model="form.projectName" />
      </n-form-item>
      <n-form-item label="Client">
        <n-input v-model="form.client" />
      </n-form-item>
      <n-form-item label="Due Date">
        <n-date-picker v-model="form.dueDate" />
      </n-form-item>
      <n-form-item>
        <n-button type="primary" native-type="submit">Submit</n-button>
      </n-form-item>
    </n-form>
  </n-modal>
</template>

<script setup>
import { ref } from 'vue'
import Table from './table.vue'
import Details from './details.vue'

const selectedUuid = ref(null)
const showModal = ref(false)
const form = ref({
  projectName: '',
  client: '',
  dueDate: null
})

function handleShowDetails(uuid) {
  selectedUuid.value = uuid
}

function handleSubmit() {
  console.log('Form submitted:', form.value)
  showModal.value = false
}
</script>

<style scoped>
.table-section {
  width: 96%;
  height: 100%;
}
.form-section {
  padding: 20px;
  height: 100%;
}
.operation-section {
  margin-top: 10px;
  margin-left: 30px;
}
</style>
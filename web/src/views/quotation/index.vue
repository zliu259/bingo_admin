<template>
  <n-split direction="horizontal" style="height: 100%" max="1200px" min="800px">
    <template #1>
      <n-scrollbar style="max-height: 100%">
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
</template>

<script setup>
import { ref } from 'vue'
import Table from './table.vue'
import Details from './details.vue'

const selectedUuid = ref(null)

function handleShowDetails(uuid) {
  selectedUuid.value = uuid
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
</style>
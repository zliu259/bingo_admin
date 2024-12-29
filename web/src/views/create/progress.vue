<template>
  <n-space vertical>
    <n-steps :current="current as number" :status="currentStatus">
      <n-step
        title="Create Project"
        description="创建项目"
      />
      <n-step
        title="Upload Files"
        description="上传文件"
      />
      <n-step
        title="Quotation"
        description="创建报价"
      />
    </n-steps>
  </n-space>
</template>

<script lang="ts">
import { defineProps } from 'vue'
const props = defineProps<{
  step: string
}>()

</script>
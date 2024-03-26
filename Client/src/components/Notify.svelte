<script lang="ts">
	// export let message: string;
	// export let type: string;
	export let showNotification: boolean = false;
</script>

{#if showNotification}
	<div
		class="z-10 bg-white p-4 rounded-xl flex flex-col gap-5 w-full m-8 justify-center items-center relative"
	>
		<div>error</div>
	</div>
{/if}

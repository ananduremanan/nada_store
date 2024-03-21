<script lang="ts">
	import '../app.css';
	import LoginPopUp from '../components/LoginPopUp.svelte';
	let isOpen: boolean = false;
</script>

<nav class="px-8 lg:px-28 py-4 flex justify-between">
	<div class="text-lg">Nada Store</div>
	<div>
		<button
			class="bg-black text-white px-2 py-1 rounded-md"
			on:click={() => {
				isOpen = !isOpen;
			}}>Login</button
		>
	</div>
</nav>
<main class="px-8 lg:px-28 relative">
	<slot />
	{#if isOpen}
		<div class="fixed inset-0 flex justify-center items-center z-50">
			<LoginPopUp on:cancel={(event) => (isOpen = event.detail)} />
		</div>
	{/if}
</main>

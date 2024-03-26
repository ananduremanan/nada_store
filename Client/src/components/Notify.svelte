<script lang="ts">
	interface notify {
		showNotification: boolean;
		message: string;
		type: string;
	}

	export let message: string;
	export let type: string;
	export let showNotification: boolean = false;

	export const notify = ({ showNotification, message, type }: notify) => {
		if (showNotification) {
			showNotification = true;
			message = message;
			type = type;
		}
	};
</script>

{#if showNotification}
	<div
		class="z-10 bg-white p-4 rounded-xl flex flex-col gap-5 w-full m-8 justify-center items-center relative"
	>
		<div>{message}</div>
	</div>
{/if}

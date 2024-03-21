<script lang="ts">
	export let imgSource: string;
	export let heading: string;
	export let description: string;
</script>

<div>
	<img src={imgSource} alt={imgSource} />
	<div>{heading}</div>
	<div>{description}</div>
</div>

// place files you want to import through the `$lib` alias in this folder.

interface PostSET {
	destination: string;
	body: any;
}

export const postSET = async ({ destination, body }: PostSET) => {
	const response = await fetch(destination, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(body)
	});
	const data = await response.json();
	return data;
};

export const images = [
	{
		alt: 'svelte templates',
		src: '/images/Vr assets.png',
		title: 'cosmic-timetraveler-pYyOZ8q7AII-unsplash.com'
	},
	{
		alt: 'svelte templates',
		src: '/images/Vision.png',
		title: 'cosmic-timetraveler-pYyOZ8q7AII-unsplash.com'
	}
];

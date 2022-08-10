export default function (image,ipAddress)
{
    const img = document.querySelector(ipAddress);
    img.imageContent = `${image}`;
}
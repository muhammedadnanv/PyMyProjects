const puppeteer = require('puppeteer');

async function convertToPDF(url, outputFilePath) {
    try {
        // Launch the browser
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        // Navigate to the URL
        await page.goto(url, { waitUntil: 'networkidle2' });

        // Create a PDF
        await page.pdf({
            path: outputFilePath,
            format: 'A4',
            printBackground: true
        });

        console.log(`PDF saved to ${outputFilePath}`);

        // Close the browser
        await browser.close();
    } catch (error) {
        console.error('Error converting website to PDF:', error);
    }
}

module.exports = convertToPDF;

const puppeteer = require('puppeteer');

async function extractMetadata(url) {
    let browser;
    try {
        browser = await puppeteer.launch({ headless: "new" });
        const page = await browser.newPage();
        await page.setUserAgent("Mozilla/5.0");
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });

        // Extract metadata
        const metadata = await page.evaluate(() => {
            const title = document.title || "No Title";
            const descriptionTag = document.querySelector('meta[name="description"]');
            const description = descriptionTag ? descriptionTag.content : "No Description";
            return { title, description };
        });

        return metadata;

    } catch (error) {
        return { error: `Failed to fetch metadata: ${error.message}` };
    } finally {
        if (browser) await browser.close();
    }
}

// Run as a standalone script (for testing)
if (require.main === module) {
    const url = process.argv[2];
    extractMetadata(url).then(console.log).catch(console.error);
}

module.exports = extractMetadata;

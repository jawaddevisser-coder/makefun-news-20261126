// News-image entry: the poster is the entry.png beside this file.
// The program copies it to the output directory the grader provides
// (MAKEFUN_OUTPUT_DIR outside the container, /output inside it).
// Node 22, standard library only.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
console.log("entry.png copied to " + outDir);

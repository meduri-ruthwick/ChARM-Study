# CHAPTER 2 - Data Acquisition, Processing, and Alignment Pipeline
# Author: Ruthwick | Thesis Scripts | IIT Gandhinagar
# Date: 24.04.25
# Description: The commands in this script handles downloading, preprocessing, alignment, and peak calling for ATAC-seq data.

# 1. Download data from ENA
echo "📥 Downloading raw data..."
wget "https://your-ena-link.fastq.gz" -O Read.fastq.gz

# 2. Preprocessing and Adapter Trimming using fastp (v0.23.4)
fastp \
  -i "READ1.fastq.gz" \
  -I "READ2.fastq.gz" \
  -o "READ1-FP.fastq.gz" \
  -O "READ2-FP.fastq.gz" \
  -w Threads \
  --html fastp_report.html \
  --json fastp_report.json

# 3. Alignment using Bowtie2 (v2.3.5.1)
bowtie2 \
  --very-sensitive-local \
  -x path/to/bowtie2_index/genome_index \
  -1 processed_READ1.fastq.gz \
  -2 processed_READ2.fastq.gz \
  -X 1000 \
  --no-mixed \
  --no-discordant \
  --no-unal \
  -t \
  -S aligned_output.sam \
  -p threads 2> alignment_stats.txt

# 4. SAM to sorted BAM using Samtools (v1.3.1)
samtools view -b -@ 8 aligned_output.sam | \
  samtools sort -n -@ 8 -o aligned_output.bam

# 5. BAM to BED conversion using Bedtools (v2.31.1)
bamToBed -bedpe -i aligned_output.bam > aligned_output.bed

# Extract final BED format with proper fields
awk 'BEGIN{OFS=FS="\t"} $4==$1 {print $1, $2, $6, $6-$2}' aligned_output.bed > aligned_final.bed

# 6. Peak Calling using MACS3 (v3.0.1)
macs3 callpeak \
  -t aligned_final.bed \
  --outdir macs3_output \
  -n atac_peaks \
  --nomodel

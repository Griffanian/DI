class Video {
  constructor(title,uploader,time){
    this.title = title
    this.uploader = uploader
    this.time = time
  }
  watch() {
    console.log(`${this.uploader} watched all ${this.time} mins of ${this.title}`)
  }
}

const newVid1 = new Video('cool','miles', 10)

newVid.watch()

const newVid2 = new Video('cool2','miles', 15)
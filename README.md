ph_1
====

Map of "Click and Drag" (original at http://xkcd.com/1110/)

<pre style="font-size:x-small;">
                               *                           *                    
                               *                          ***                   
                               **                        *****                  
                               *                        *******                 
                              **  **                   *********                
           *                 ****  ****         **    ***********      *        
*********************************S**********************************************
                *          *           *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *     *                *                                        
                **********             *                                        
                         ***           *                                        
                          **********   *                                        
                                **     *                                        
                                 *    ***                                       
                                 *** ****                                       
                                   **   *                                       
                                    *****                                       
</pre>

Riddle
===

**Question**: Where are Peter Naur, Anders Hejlsberg, Bjarne Stoustrup, Mikkel Thorup and Vitus Bering?

Post your answer on the [page for this pantherhash](http://pantherhash.com/ph_1/ "Click and Drag")

Hints
===

**Hint 1**

See `ph_1.py`

Downloading and analysing XKCD: Click and Drag
===

The script `download_xkcd1110.py` crawls the XKCD Click and Drag comic: http://xkcd.com/1110, and downloads all the images.

It discovers various properties of the comic.

**World dimensions**

'1n1e' type coordinates used in the comic are mapped to '(0,0)' type coordinates.

Minimum and maximum indexes of the Click and Drag world are: 

* min x: -33
* max x:  47 
* min y: -19
* max y:   7

**Image dimenensions**

If all the images of Click and Drag where combined into a single image, it would have these dimensions:

* width: 163840
* height: 53248

**ASCII-art map of XKCD Click and Drag world**

Overview map of images found using depth first search (see `download_xkcd1110.py`):

"S" denotes the landing image when you look at the comic.

<pre>
                               *                           *                    
                               *                          ***                   
                               **                        *****                  
                               *                        *******                 
                              **  **                   *********                
           *                 ****  ****         **    ***********      *        
*********************************S**********************************************
                *          *           *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *                      *                                        
                *     *                *                                        
                **********             *                                        
                         ***           *                                        
                          **********   *                                        
                                **     *                                        
                                 *    ***                                       
                                 *** ****                                       
                                   **   *                                       
                                    *****                                       
</pre>


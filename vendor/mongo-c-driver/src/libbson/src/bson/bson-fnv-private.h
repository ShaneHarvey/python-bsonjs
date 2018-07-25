/*
 * Please do not copyright this code.  This code is in the public domain.
 *
 * LANDON CURT NOLL DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
 * INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
 * EVENT SHALL LANDON CURT NOLL BE LIABLE FOR ANY SPECIAL, INDIRECT OR
 * CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
 * USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
 * OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
 * PERFORMANCE OF THIS SOFTWARE.
 *
 * By:
 *  chongo <Landon Curt Noll> /\oo/\
 *      http://www.isthe.com/chongo/
 */

#ifndef MONGO_C_DRIVER_BSON_FNV_PRIVATE_H
#define MONGO_C_DRIVER_BSON_FNV_PRIVATE_H

#include "bson.h"

uint32_t
_mongoc_fnv_24a_str (char *str);

#endif /* MONGO_C_DRIVER_BSON_FNV_PRIVATE_H */

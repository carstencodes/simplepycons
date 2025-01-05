#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class RottenTomatoesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rottentomatoes"

    @property
    def original_file_name(self) -> "str":
        return "rottentomatoes.svg"

    @property
    def title(self) -> "str":
        return "Rotten Tomatoes"

    @property
    def primary_color(self) -> "str":
        return "#FA320A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rotten Tomatoes</title>
     <path d="M5.866 0L4.335 1.262l2.082 1.8c-2.629-.989-4.842
 1.4-5.012 2.338 1.384-.323 2.24-.422 3.344-.335-7.042 4.634-4.978
 13.148-1.434 16.094 5.784 4.612 13.77 3.202 17.91-1.316C27.26 13.363
 22.993.65 10.86 2.766c.107-1.17.633-1.503
 1.243-1.602-.89-1.493-3.67-.734-4.556 1.374C7.52 2.602 5.866 0 5.866
 0zM4.422 7.217H6.9c2.673 0 2.898.012 3.55.202 1.06.307 1.868.973
 2.313 1.904.05.106.092.206.13.305l7.623.008.027
 2.912-2.745-.024v7.549l-2.982-.016v-7.522l-2.127.016a2.92 2.92 0 0
 1-1.056 1.134c-.287.176-.3.19-.254.264.127.2 2.125 3.642 2.125
 3.659l-3.39.019-2.013-3.376c-.034-.047-.122-.068-.344-.084l-.297-.02.037
 3.48-3.075-.038zm3.016 2.288l.024.338c.014.186.024.729.024
 1.206v.867l.582-.025c.32-.013.695-.049.833-.078.694-.146 1.048-.478
 1.087-1.018.027-.378-.063-.636-.303-.87-.318-.309-.761-.416-1.733-.418Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Rotte'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []

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


class DistroboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "distrobox"

    @property
    def original_file_name(self) -> "str":
        return "distrobox.svg"

    @property
    def title(self) -> "str":
        return "Distrobox"

    @property
    def primary_color(self) -> "str":
        return "#4F433C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Distrobox</title>
     <path d="M12 0a2.596 2.596 0 0 0-1.298.348L2.558 5.05A2.596 2.596
 0 0 0 1.26 7.298v9.404a2.596 2.596 0 0 0 1.298 2.248l8.144
 4.702a2.596 2.596 0 0 0 2.596 0l8.144-4.702a2.596 2.596 0 0 0
 1.298-2.248V7.298a2.596 2.596 0 0 0-1.298-2.248L13.298.348A2.596
 2.596 0 0 0 12 0Zm-.15.9a.865.865 0 0 1 .583.102l7.876 4.548a.288.288
 0 0 1 0 .5l-7.876 4.547a.865.865 0 0 1-.866 0L3.691 6.049a.288.288 0
 0 1 0-.5l7.876-4.547A.865.865 0 0 1 11.85.9zm4.126 4.069-2.666
 1.54.69.398 2.667-1.539zm-5.025.4-3.618.862.846.489 2.239-.634-1.083
 1.301.846.489 1.493-2.089zM2.498 7.746a.288.288 0 0 1 .194.034l7.876
 4.547a.865.865 0 0 1 .433.75v9.095a.288.288 0 0
 1-.433.25l-7.876-4.548a.865.865 0 0 1-.433-.75V8.03a.288.288 0 0 1
 .239-.284zm19.004 0a.288.288 0 0 1 .239.284v9.095a.865.865 0 0
 1-.433.749l-7.876 4.547a.288.288 0 0 1-.433-.25v-9.094a.865.865 0 0 1
 .433-.75l7.876-4.547a.288.288 0 0 1 .194-.034zm-17.58 3.529v.977l1.67
 1.622-1.67-.288v.977l2.556.249v-.835zm13.296
 2.878-2.555.248v.977l1.668-.304-1.668
 1.639v.977l2.555-2.703zm2.86.85-2.667 1.539v.798l2.666-1.54zM6.67
 16.589v.798l2.666 1.54v-.798z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/89luca89/distrobox/blob/71
cf8295fb74bb2805904cb3fb497556331ec169/docs/assets/brand/distrobox-log'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/89luca89/distrobox/blob/71
cf8295fb74bb2805904cb3fb497556331ec169/docs/assets/brand/svg/distrobox'''

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

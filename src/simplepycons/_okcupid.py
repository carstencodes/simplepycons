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


class OkcupidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "okcupid"

    @property
    def original_file_name(self) -> "str":
        return "okcupid.svg"

    @property
    def title(self) -> "str":
        return "okcupid"

    @property
    def primary_color(self) -> "str":
        return "#0500BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>okcupid</title>
     <path d="M11.287 5.336c-1.656 0-2.609.886-2.831
 2.632l-.106.804a.275.275 0
 01-.382.218c-.67-.294-1.472-.45-2.397-.45C2.24 8.54 0 10.794 0 14.146
 0 16.933 1.738 18.6 4.65 18.6c1.213 0 2.275-.27 3.142-.766a.268.268 0
 01.323.045c.452.44 1.108.688 1.906.688.74 0 1.281-.072
 1.702-.228l.489-.18a.28.28 0 01.248.03c.371.234.84.378 1.456.378
 1.138 0 1.927-.218 2.474-.535a.275.275 0
 01.272-.005c.19.101.394.188.61.264.623.244 1.355.374 2.198.374 3.635
 0 4.38-1.791 4.38-2.838
 0-.515-.127-1.04-.473-1.435-.01-.013-.027-.023-.038-.04-.387-.539-1.147-.349-1.324-.701-.09-.181-.016-.494.59-.466
 1.09.05 1.395-1.399 1.395-2.172 0-.954-.449-2.556-3.455-2.556-1.144
 0-2.151.247-2.993.697-.08.039-.162.076-.241.116a.268.268 0
 01-.298-.034c-.435-.379-1.115-.661-2.177-.661-.225
 0-.432.012-.625.039a.275.275 0
 01-.312-.31l.118-.888.097-.727a.277.277 0
 00-.106-.257l-.582-.447c-.735-.563-1.656-.648-2.14-.648zm.013
 1.545c.46 0 .92.115 1.2.33l-.773 5.784c1.956-2.712 2.136-2.876
 3.122-2.876 1.036 0 1.397.296 1.397.887 0
 .345-.098.575-.263.756-.246-.016-.493-.016-.69-.016-.345
 0-.542.082-1.512 1.413L14.9 15.18c.082.132.164.247.345.247.148 0
 .395-.017.592-.066.164.115.23.346.23.559 0 .772-.773 1.101-2.137
 1.101-.64 0-.87-.23-1.216-.97L11.612 13.8l-.411
 3.09c-.312.115-.821.131-1.167.131-.723 0-1.051-.295-1.051-.92
 0-.181.032-.493.098-.937l.92-7c.132-1.036.477-1.283
 1.299-1.283zm-5.716 3.204c2.383 0 3.221 1.184 3.221 2.943 0
 2.482-1.512 4.026-4.141 4.026-1.874 0-3.107-.822-3.107-2.909 0-2.432
 1.48-4.06 4.027-4.06zm14.718.017c1.561 0 1.939.477 1.939 1.101 0
 .345-.115.543-.329.707-.377-.115-.772-.18-1.38-.18-1.184
 0-1.857.69-1.857 2.169 0 1.084.328 1.479 1.199 1.479.493 0 1.068-.116
 1.693-.345.23.115.345.443.345.69 0 .838-.756 1.331-2.613 1.331-1.988
 0-3.057-.805-3.057-2.893 0-2.596 1.578-4.059 4.06-4.059zM5.452
 11.68c-1.002 0-1.56 1.019-1.56 2.383 0 .986.279 1.43 1.084 1.43.903 0
 1.594-.872 1.594-2.367 0-.969-.263-1.446-1.117-1.446z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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

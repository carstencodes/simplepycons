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


class FlipkartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flipkart"

    @property
    def original_file_name(self) -> "str":
        return "flipkart.svg"

    @property
    def title(self) -> "str":
        return "Flipkart"

    @property
    def primary_color(self) -> "str":
        return "#2874F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flipkart</title>
     <path d="M3.833 1.333a.993.993 0 0 0-.333.061V1c0-.551.449-1
 1-1h14.667c.551 0 1 .449 1 1v.333H3.833zm17.334 2.334H2.833c-.551 0-1
 .449-1 1V23c0 .551.449 1 1 1h7.3l1.098-5.645h-2.24c-.051
 0-5.158-.241-5.158-.241l4.639-.327-.078-.366-1.978-.285
 1.882-.158-.124-.449-3.075-.467s3.341-.373
 3.392-.373h3.232l.247-1.331c.289-1.616.945-2.807 1.973-3.693
 1.033-.892 2.344-1.332 3.937-1.332.643 0 1.053.151
 1.231.463.118.186.201.516.279.859.074.352.14.671.095.903-.057.345-.461.465-1.197.465h-.253c-1.327
 0-2.134.763-2.405 2.31l-.243 1.355h1.54c.574 0 .781.402.622
 1.306-.17.941-.539 1.36-1.111 1.36H14.9L13.804 24h7.362c.551 0 1-.449
 1-1V4.667a1 1 0 0 0-.999-1zM20.5 2.333A.334.334 0 0 0 20.167
 2H3.833a.334.334 0 0 0-.333.333V3h17v-.667z" />
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

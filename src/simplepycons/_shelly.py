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


class ShellyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shelly"

    @property
    def original_file_name(self) -> "str":
        return "shelly.svg"

    @property
    def title(self) -> "str":
        return "Shelly"

    @property
    def primary_color(self) -> "str":
        return "#4495D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shelly</title>
     <path d="M12 0C5.373 0 0 5.373 0 12a12 12 0 0 0 .033.88c1.07-.443
 2.495-.679 4.322-.679h5.762c-.167.61-.548 1.087-1.142
 1.436-.532.308-1.14.463-1.823.463h-.927c-.89
 0-1.663.154-2.32.463-.859.403-1.286 1-1.286 1.789 0 .893.59 1.594
 1.774 2.1a7.423 7.423 0 0 0 2.927.581c1.318 0 2.416-.29 3.297-.867
 1.024-.664 1.535-1.616 1.535-2.857
 0-.854-.325-2.08-.976-3.676-.65-1.597-.975-2.837-.975-3.723 0-2.79
 2.305-4.233 6.916-4.324.641-.01 1.337-.005 1.916-.004.593 0 1.144.05
 1.66.147A12 12 0 0 0 12 0zm4.758 5.691c-1.206 0-1.809.502-1.809 1.506
 0 .514.356 1.665 1.067 3.451.71 1.787 1.064 3.186 1.064 4.198 0
 2.166-1.202 3.791-3.607 4.875-1.794.797-3.892 1.197-6.297 1.197-1.268
 0-2.442-.114-3.543-.316A12 12 0 0 0 12 24c6.627 0 12-5.373 12-12a12
 12 0 0 0-.781-4.256 3.404 3.404 0 0
 1-.832.77h-4.371l1.425-2.828a299.94 299.94 0 0 0-2.683.005Z" />
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

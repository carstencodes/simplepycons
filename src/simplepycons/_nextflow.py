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


class NextflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nextflow"

    @property
    def original_file_name(self) -> "str":
        return "nextflow.svg"

    @property
    def title(self) -> "str":
        return "Nextflow"

    @property
    def primary_color(self) -> "str":
        return "#0DC09D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nextflow</title>
     <path d="M.005 4.424V0c6.228.259 11.227 5.268 11.477
 11.506H7.058C6.828 7.715 3.786 4.673.005 4.424m7.082
 8.089h4.424C11.251 18.741 6.242 23.741.005 23.99v-4.423c3.79-.231
 6.832-3.273 7.082-7.054m9.826-1.036h-4.424C12.749 5.249 17.758.25
 23.995 0v4.424c-3.79.23-6.832 3.263-7.082 7.053m7.082
 8.099V24c-6.228-.259-11.227-5.268-11.477-11.506h4.424c.23 3.791 3.272
 6.833 7.053 7.082" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/seqeralabs/logos/blob/a8d4'''

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

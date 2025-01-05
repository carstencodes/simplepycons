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


class GitLfsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitlfs"

    @property
    def original_file_name(self) -> "str":
        return "gitlfs.svg"

    @property
    def title(self) -> "str":
        return "Git LFS"

    @property
    def primary_color(self) -> "str":
        return "#F64935"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Git LFS</title>
     <path d="M11.967.304L0 7.215v9.68l11.79
 6.802V14.02l11.96-6.91-4.383-2.53-11.959
 6.905v3.887l-2.775-1.601V9.886l11.965-6.91zM24 7.545L12.29
 14.31v9.387L24 16.929V7.547z" />
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

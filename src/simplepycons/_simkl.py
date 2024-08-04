#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class SimklIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simkl"

    @property
    def original_file_name(self) -> "str":
        return "simkl.svg"

    @property
    def title(self) -> "str":
        return "Simkl"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Simkl</title>
     <path d="M3.84 0A3.832 3.832 0 0 0 0 3.84v16.32A3.832 3.832 0 0 0
 3.84 24h16.32A3.832 3.832 0 0 0 24 20.16V3.84A3.832 3.832 0 0 0 20.16
 0zm8.567 4.11c2.074 0 3.538.061 4.393.186 1.127.168 1.94.46
 2.438.877.672.578 1.009 1.613 1.009 3.104 0
 .161-.004.417-.01.768h-4.234c-.014-.358-.039-.607-.074-.746-.098-.41-.42-.64-.966-.692-.484-.043-1.66-.066-3.53-.066-1.85
 0-2.946.056-3.289.165-.385.133-.578.474-.578 1.024 0
 .528.203.851.61.969.343.095 1.887.187 4.633.275 2.487.073 4.073.165
 4.76.275.693.11 1.244.275 1.654.495.41.22.737.532.983.936.37.595.557
 1.552.557 2.873 0 1.475-.182 2.557-.546 3.247-.364.683-.96
 1.149-1.785 1.398-.812.25-3.05.374-6.71.374-2.226
 0-3.832-.062-4.82-.187-1.204-.147-2.068-.434-2.593-.86-.567-.456-.903-1.1-1.008-1.93a10.522
 10.522 0 0 1-.085-1.434v-.789H7.44c-.007.74.136 1.216.43
 1.428.154.102.33.167.525.203.196.037.54.063 1.03.077a166.2 166.2 0 0
 0 2.405.022c1.862-.007 2.94-.018 3.234-.033.553-.044.917-.12
 1.092-.23.245-.161.368-.52.368-1.077
 0-.38-.078-.648-.231-.802-.211-.212-.712-.325-1.503-.34-.547
 0-1.688-.044-3.425-.132-1.794-.088-2.956-.14-3.488-.154-1.387-.044-2.364-.212-2.932-.505-.728-.373-1.205-1.01-1.429-1.91-.126-.498-.189-1.15-.189-1.956
 0-1.698.309-2.895.925-3.59.462-.527 1.163-.875 2.102-1.044.848-.146
 2.865-.22 6.053-.22z" />
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